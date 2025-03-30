import pandas as pd
import h5py as h5


#Tyler
file_path = "data/tyler-jumping-raw-data.csv"
d_tyler_jump = pd.read_csv(file_path)

file_path = "data/tyler-walking-raw-data.csv"
d_tyler_walk = pd.read_csv(file_path)


#Mukit
file_path = "data/mukit-jumping-raw-data.csv"
mukit_jump = pd.read_csv(file_path)

file_path = "data/mukit-walking-raw-data.csv"
mukit_walk = pd.read_csv(file_path)

#Sydney
file_path = "data/Sydney-JumpingTrial1inHand.csv"
sydney_jump1 = pd.read_csv(file_path)
file_path = "data/Sydney-JumpingTrial2inPocket.csv"
sydney_jump2 = pd.read_csv(file_path)
file_path = "data/Sydney-JumpingTrial3inJacket.csv"
sydney_jump3 = pd.read_csv(file_path)

file_path = "data/Sydney-WalkingTrial1inHand.csv"
sydney_walk1 = pd.read_csv(file_path)
file_path = "data/Sydney-WalkingTrial2inPocket.csv"
sydney_walk2 = pd.read_csv(file_path)
file_path = "data/Sydney-WalkingTrial3inJacket.csv"
sydney_walk3 = pd.read_csv(file_path)

#Combine Jump
time_offset1_2 = sydney_jump1['Time (s)'].iloc[-1] #move graph 2 up
sydney_jump2['Time (s)'] += time_offset1_2
time_offset2_3 = sydney_jump2['Time (s)'].iloc[-1] #move graph 3 up
sydney_jump3['Time (s)'] += time_offset2_3

#Combine Walk
time_offset1_2 = sydney_walk1['Time (s)'].iloc[-1] #move graph 2 up
sydney_walk2['Time (s)'] += time_offset1_2
time_offset2_3 = sydney_walk2['Time (s)'].iloc[-1] #move graph 3 up
sydney_walk3['Time (s)'] += time_offset2_3
#Combine
sydney_jump = pd.concat([sydney_jump1, sydney_jump2, sydney_jump3])
sydney_walk = pd.concat([sydney_walk1, sydney_walk2, sydney_walk3])

with h5.File('./data.h5', 'w') as hdf:

    #Tyler Folder
    rd_t = hdf.create_group('/raw_data/tyler')
    rd_t.create_dataset('jumping', data=d_tyler_jump)
    rd_t.create_dataset('walking', data=d_tyler_walk)


    ppd_t = hdf.create_group('/pre_processed_data/tyler')
    # put code here

    sd_tr = hdf.create_group('/segmented_data/train')
    # put code here

    sd_te = hdf.create_group('/segmented_data/test')
    # put code here



    #Mukit Folder
    rd_t = hdf.create_group('/raw_data/mukit')
    rd_t.create_dataset('jumping', data=mukit_jump)
    rd_t.create_dataset('walking', data=mukit_walk)

    ppd_t = hdf.create_group('/pre_processed_data/mukit')
    # put code here


    #Syndey Folder
    rd_t = hdf.create_group('/raw_data/sydney')
    rd_t.create_dataset('jumping', data=sydney_jump)
    rd_t.create_dataset('walking', data=sydney_walk)

    ppd_t = hdf.create_group('/pre_processed_data/sydney')
    # put code here 
