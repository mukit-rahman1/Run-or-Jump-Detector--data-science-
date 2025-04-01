import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, log_loss
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import log_loss

'''
steps to follow

load and get features and non features as arrays
Make X 2D features and Y 1D mapped to 0 and 1. split same way 90/10.
Normalize features using Z score
Train logistic regression and plot loss at different max_iter values
display graph
evaluate using library functions
Save model and scaler method as tuple
'''

# load
df = pd.read_csv("features.csv")

non_features = ['person', 'activity']
feature_cols = [col for col in df.columns if col not in non_features]

X = df[feature_cols].values
y = df['activity'].map({'walking': 0, 'jumping': 1}).values

# Split the data (randomly but stratified)
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42, stratify=y
)

# Normalize (fit only on training data)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train_raw)
X_test = scaler.transform(X_test_raw)


#train logistic regression and plot loss at different max_iter values
iter_values = [1, 5, 10, 20, 50, 100, 200, 500]
losses = []

for max_iter in iter_values:
    model = LogisticRegression(max_iter=max_iter, solver='lbfgs')
    model.fit(X_train, y_train)
    y_proba = model.predict_proba(X_train)
    loss = log_loss(y_train, y_proba)
    losses.append(loss)


#plot the losses 
plt.plot(iter_values, losses, marker='o')
plt.title("Training Loss vs Iterations (LogisticRegression)")
plt.xlabel("max_iter")
plt.ylabel("Log Loss")
plt.grid(True)
plt.tight_layout()
plt.show()

# Evaulate using library functions
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"accuracy: {acc *100:.2f}%")

#save model and scaler method as tuple
joblib.dump((model, scaler), "final_model.pkl")
