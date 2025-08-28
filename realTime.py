import requests, time, collections
import numpy as np
from joblib import load

PHONE_URL  = "http://<phone-ip>:8080/get"
MODEL_PATH = "rt_model.pkl"                 # contains (scaler, model)
WINDOW_SEC = 0.8
HOP_SEC    = 0.2
POLL_SLEEP = 0.05

scaler, model = load(MODEL_PATH)
buf = collections.deque(maxlen=5000)

def feats(win):
    ax, ay, az = win[:,1], win[:,2], win[:,3]
    mag = np.sqrt(ax*ax + ay*ay + az*az)
    def stats(v):
        mn=v.min(); mx=v.max(); mean=v.mean(); med=np.median(v)
        var=v.var(); std=v.std(); rng=mx-mn
        skew = ((v-mean)**3).mean() / (std**3 + 1e-8)
        return [mn,mx,rng,mean,med,var,std,skew]
    return np.array(stats(ax)+stats(ay)+stats(az)+stats(mag), dtype=np.float32).reshape(1,-1)

last = 0.0
while True:
    try:
        j = requests.get(PHONE_URL, timeout=0.25).json()
        t  = j["buffer"]["time"]["buffer"]
        ax = j["buffer"]["accX"]["buffer"]
        ay = j["buffer"]["accY"]["buffer"]
        az = j["buffer"]["accZ"]["buffer"]
        for i in range(len(t)):
            buf.append((float(t[i]), float(ax[i]), float(ay[i]), float(az[i])))
    except Exception:
        pass

    now = time.time()
    if (now - last) >= HOP_SEC and len(buf) > 10:
        last = now
        arr = np.array(list(buf), dtype=np.float32)
        win = arr[arr[:,0] >= arr[-1,0] - WINDOW_SEC]
        if len(win) >= 10:
            X = feats(win)
            X = scaler.transform(X)
            proba = model.predict_proba(X)[0]
            idx = int(np.argmax(proba))
            label = model.classes_[idx]
            print(f"{label}  p={proba[idx]:.2f}  raw={np.round(proba,2)}")
    time.sleep(POLL_SLEEP)
