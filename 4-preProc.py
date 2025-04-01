import pandas as pd
import h5py
import numpy as np


people = ['mukit', 'tyler', 'sydney']
window_size = 50

'''
steps to follow


load
convert to dataframe
fill NaNs
apply rolling
fill and handle edge NaNs
save to hdf5
'''



#create output hdf5
with h5py.File('data.h5', 'a') as in_hdf:    #open existing hdf5 to write new
    for person in people:
        '''
        WALKING PRE PROCESSING
        '''
        #load raw data
        dataset_path = f'/raw_data/{person}/walking'
        raw_data = in_hdf[dataset_path][()]

        #convert to data frame
        df = pd.DataFrame(raw_data, columns=['time', 'x', 'y', 'z', 'absolute'])

        #handle missing
        df.interpolate(method='linear', inplace=True)
        df.fillna(method='bfill', inplace=True)
        df.fillna(method='ffill', inplace=True)

        #apply rolling
        df['x'] = df['x'].rolling(window=window_size).mean()
        df['y'] = df['y'].rolling(window=window_size).mean()
        df['z'] = df['z'].rolling(window=window_size).mean()
        df['absolute'] = df['absolute'].rolling(window=window_size).mean()

        #Handle edge NaN incase rolling created any
        df.interpolate(method='linear', inplace=True)
        df.fillna(method='bfill', inplace=True)
        df.fillna(method='ffill', inplace=True)

        #save to hdf5
        preprocessed = df.values
        in_hdf.create_dataset(f'/processed_data/{person}/walking', data=preprocessed)


        '''
        JUMPING PRE PROCESSING
        '''
        #load raw data
        dataset_path = f'/raw_data/{person}/jumping'
        raw_data = in_hdf[dataset_path][()]

        #convert to data frame
        df = pd.DataFrame(raw_data, columns=['time', 'x', 'y', 'z', 'absolute'])

        #handle missing
        df.interpolate(method='linear', inplace=True)
        df.fillna(method='bfill', inplace=True)
        df.fillna(method='ffill', inplace=True)

        #apply rolling
        df['x'] = df['x'].rolling(window=window_size).mean()
        df['y'] = df['y'].rolling(window=window_size).mean()
        df['z'] = df['z'].rolling(window=window_size).mean()
        df['absolute'] = df['absolute'].rolling(window=window_size).mean()

        #Handle edge NaN incase rolling created any
        df.interpolate(method='linear', inplace=True)
        df.fillna(method='bfill', inplace=True)
        df.fillna(method='ffill', inplace=True)

        #save to hdf5
        preprocessed = df.values
        in_hdf.create_dataset(f'/processed_data/{person}/jumping', data=preprocessed)

print("Preprocessing complete...")