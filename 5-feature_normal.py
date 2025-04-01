import pandas as pd
import numpy as np
import h5py
from scipy.stats import skew, kurtosis
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Configurations
people = ['mukit', 'tyler', 'sydney']
activities = ['walking', 'jumping']
Hz = 100
window_duration = 5
window_size = Hz * window_duration

features = []


'''
steps to follow

Extract features:
load by reading hdf5 preprocessed_data/{person}/{activity}
extract features by windowing and sending it to function
function takes window and returns features using pandas and scipy funcs (mean, std, min, max, skew, kurtosis, var, range, median, rms). note sqrt is numpy
repeat function for length of data / 500 (window size)
repeat above for each activity and person
append features to dictionary and save as features.csv

Normalize features:
label the non feature columns
choose standard scaler Z score standardization
Standardize features, replace, save as normalized_features.csv

Split or Segment Data:
load 2D features array into X. load 1D labels array into Y and map to 0 and 1. split to 90/10, randomness as 42, keep class distribution preserved(avoid having only walking as training etc.).
save as hdf5 in segmented_data/train/features and segmented_data/train/labels. save as hdf5 in segmented_data/test/features and segmented_data/test/labels
'''




'''
Extract Features
'''
def extract_features(window):
    df = pd.DataFrame(window, columns=['time', 'x', 'y', 'z', 'absolute'])
    feats = {}
    for col in ['absolute']:
        data = df[col]
        feats[f'{col}_mean'] = data.mean()
        feats[f'{col}_std'] = data.std()
        feats[f'{col}_min'] = data.min()
        feats[f'{col}_max'] = data.max()
        feats[f'{col}_skew'] = skew(data)
        feats[f'{col}_kurtosis'] = kurtosis(data)
        feats[f'{col}_var'] = data.var()
        feats[f'{col}_range'] = data.max() - data.min()
        feats[f'{col}_median'] = data.median()
        feats[f'{col}_rms'] = np.sqrt(data.mean())
    return feats

# ---- Extract features from processed data ----
with h5py.File('data.h5', 'r') as hdf:
    for person in people:
        for activity in activities:
            path = f'/processed_data/{person}/{activity}'
            data = hdf[path][()]
            num_windows = len(data) // window_size

            for i in range(num_windows):
                start = i * window_size
                end = start + window_size
                window = data[start:end]
                feat = extract_features(window)
                feat['person'] = person
                feat['activity'] = activity
                features.append(feat)

# save csv
df = pd.DataFrame(features)
df.to_csv("features.csv", index=False)
print("regular features saved")




'''NORMALIZE FEATURES'''
non_features = ['person', 'activity']
feature_cols = [col for col in df.columns if col not in non_features]

scaler = StandardScaler() # Choose Z score
X_scaled = scaler.fit_transform(df[feature_cols]) # Standardize features

df[feature_cols] = X_scaled #replace

df.to_csv("normalized_features.csv", index=False) #save



'''SPLIT OR SEGMENT DATA'''
X = df[feature_cols].values
y = df['activity'].map({'walking': 0, 'jumping': 1}).values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42, stratify=y
)

# ---- Save to HDF5 ----
with h5py.File('data.h5', 'a') as hdf:
    for path in [
        '/segmented_data/train/features', '/segmented_data/train/labels',
        '/segmented_data/test/features', '/segmented_data/test/labels'
    ]:
        if path in hdf:
            del hdf[path]

    hdf.create_dataset('/segmented_data/train/features', data=X_train)
    hdf.create_dataset('/segmented_data/train/labels', data=y_train)
    hdf.create_dataset('/segmented_data/test/features', data=X_test)
    hdf.create_dataset('/segmented_data/test/labels', data=y_test)

print("extraction complete... \n normalization complete... \n segmentation complete... \n ready to initiate model training")
