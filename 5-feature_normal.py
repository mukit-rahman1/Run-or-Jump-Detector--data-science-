import h5py
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

#Function to extract features
def extract_features(person):
    #load and set as dataframe
    df = pd.DataFrame(person, columns=['time', 'x', 'y', 'z', 'absolute'])

    #initalize empty dictionary
    features = {}

    #extract
    for i in ['absolute']:
        data = df[i]

        features[f'{i}_mean'] = data.mean()
        features[f'{i}_std'] = data.std()
        features[f'{i}_min'] = data.min()
        features[f'{i}_max'] = data.max()
        features[f'{i}_skew'] = skew(data)
        features[f'{i}_kurtosis'] = kurtosis(data)
        features[f'{i}_var'] = data.var()
        features[f'{i}_range'] = data.max() - data.min()
        features[f'{i}_median'] = data.median()
        features[f'{i}_rms'] = np.sqrt(data.mean())

    return features



window_duration = 5
people = ['mukit', 'tyler', 'sydney']
activities = ['jumping', 'walking']

features = []

with h5py.File('pre_processed_data.h5', 'r') as hdf:
    for person in people:
        for activity in activities:
            dataset_path = f'/processed_data/{person}/{activity}'
            person_data = hdf[dataset_path][()]
            
            total = len(person_data)
            numberOfWindows = total // window_duration
            
            for i in range(numberOfWindows):
                start = i * window_duration
                end = start + window_duration
                window = person_data[start:end]

                feats = extract_features(window)
                feats['person'] = person
                feats['activity'] = activity
                features.append(feats)

#convert list of dictionaries to dataframe
features_df = pd.DataFrame(features)

#save to csv
features_df.to_csv('features.csv', index=False)
        
