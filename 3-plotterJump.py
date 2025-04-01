import matplotlib.pyplot as plt
import h5py
import numpy as np


'''
MUKIT
'''
with h5py.File('data.h5', 'r') as hdf:
    group_mukit_jump = hdf['/raw_data/mukit']
    data_mukit_jump = group_mukit_jump['jumping'][()] #load the dataset

    group_mukit_walk = hdf['/raw_data/mukit']
    data_mukit_walk = group_mukit_walk['walking'][()] #load the datase
#extract coloumns
time_mukit_jump = data_mukit_jump[:, 0]
absolute_mukit_jump = data_mukit_jump[:, 4]

time_mukit_walk = data_mukit_walk[:, 0]
absolute_mukit_walk = data_mukit_walk[:, 4]

#plot graphs
plt.figure(figsize=(12,8))
fig = plt.subplot(3,1,1)

#plots
plt.plot(time_mukit_jump, absolute_mukit_jump, label='Combined Acceleration Jumping', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Combined Acceleration (m/s^2)')
plt.title('Mukit Combined Acceleration vs Time (raw)')
plt.grid(True)

plt.plot(time_mukit_walk, absolute_mukit_walk, label='Combined Acceleration Walking', color='b')
plt.legend()



'''
YOUNG T
'''
with h5py.File('data.h5', 'r') as hdf:
    group_tyler_jump = hdf['/raw_data/tyler']
    data_tyler_jump = group_tyler_jump['jumping'][()] #load the dataset

    group_tyler_walk = hdf['/raw_data/tyler']
    data_tyler_walk = group_tyler_walk['walking'][()] #load the datase
#extract coloumns
time_tyler_jump = data_tyler_jump[:, 0]
absolute_tyler_jump = data_tyler_jump[:, 4]

time_tyler_walk = data_tyler_walk[:, 0]
absolute_tyler_walk = data_tyler_walk[:, 4]

#plot graphs
fig = plt.subplot(3,1,2)

#plots
plt.plot(time_tyler_jump, absolute_tyler_jump, label='Combined Acceleration Jumping', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Combined Acceleration (m/s^2)')
plt.title('Tyler Combined Acceleration vs Time (raw)')
plt.grid(True)

plt.plot(time_tyler_walk, absolute_tyler_walk, label='Combined Acceleration Walking', color='b')
plt.legend()

'''
SYD YAPPER
'''
with h5py.File('data.h5', 'r') as hdf:
    group_sydney_jump = hdf['/raw_data/sydney']
    data_sydney_jump = group_sydney_jump['jumping'][()] #load the dataset

    group_sydney_walk = hdf['/raw_data/sydney']
    data_sydney_walk = group_sydney_walk['walking'][()] #load the datase
#extract coloumns

time_sydney_jump = data_sydney_jump[:, 0]
absolute_sydney_jump = data_sydney_jump[:, 4]

time_sydney_walk = data_sydney_walk[:, 0]
absolute_sydney_walk = data_sydney_walk[:, 4]

#plot graphs
fig = plt.subplot(3,1,3)

#plots
plt.plot(time_sydney_jump, absolute_sydney_jump, label='Combined Acceleration Jumping', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Combined Acceleration (m/s^2)')
plt.title('Sydney Combined Acceleration vs Time (raw)')
plt.grid(True)

plt.plot(time_sydney_walk, absolute_sydney_walk, label='Combined Acceleration Walking', color='b')
plt.legend()
plt.show()

'''
PRE PROCESSING PLOTS
'''

plt.figure(figsize=(12, 8))

# --- MUKIT ---
with h5py.File('data.h5', 'r') as hdf:
    data_mukit_jump = hdf['/processed_data/mukit/jumping'][()]
    data_mukit_walk = hdf['/processed_data/mukit/walking'][()]

time_mukit_jump = data_mukit_jump[:, 0]
absolute_mukit_jump = data_mukit_jump[:, 4]

time_mukit_walk = data_mukit_walk[:, 0]
absolute_mukit_walk = data_mukit_walk[:, 4]

plt.subplot(3, 1, 1)
plt.plot(time_mukit_jump, absolute_mukit_jump, label='Jumping', color='r')
plt.plot(time_mukit_walk, absolute_mukit_walk, label='Walking', color='b')
plt.title('Mukit Combined Acceleration vs Time (preprocessed)')
plt.xlabel('Time (s)')
plt.ylabel('Combined Acceleration (m/s²)')
plt.grid(True)
plt.legend()

# --- TYLER ---
with h5py.File('data.h5', 'r') as hdf:
    data_tyler_jump = hdf['/processed_data/tyler/jumping'][()]
    data_tyler_walk = hdf['/processed_data/tyler/walking'][()]

time_tyler_jump = data_tyler_jump[:, 0]
absolute_tyler_jump = data_tyler_jump[:, 4]

time_tyler_walk = data_tyler_walk[:, 0]
absolute_tyler_walk = data_tyler_walk[:, 4]

plt.subplot(3, 1, 2)
plt.plot(time_tyler_jump, absolute_tyler_jump, label='Jumping', color='r')
plt.plot(time_tyler_walk, absolute_tyler_walk, label='Walking', color='b')
plt.title('Tyler Combined Acceleration vs Time (preprocessed)')
plt.xlabel('Time (s)')
plt.ylabel('Combined Acceleration (m/s²)')
plt.grid(True)
plt.legend()

# --- SYDNEY ---
with h5py.File('data.h5', 'r') as hdf:
    data_sydney_jump = hdf['/processed_data/sydney/jumping'][()]
    data_sydney_walk = hdf['/processed_data/sydney/walking'][()]

time_sydney_jump = data_sydney_jump[:, 0]
absolute_sydney_jump = data_sydney_jump[:, 4]

time_sydney_walk = data_sydney_walk[:, 0]
absolute_sydney_walk = data_sydney_walk[:, 4]

plt.subplot(3, 1, 3)
plt.plot(time_sydney_jump, absolute_sydney_jump, label='Jumping', color='r')
plt.plot(time_sydney_walk, absolute_sydney_walk, label='Walking', color='b')
plt.title('Sydney Combined Acceleration vs Time (preprocessed)')
plt.xlabel('Time (s)')
plt.ylabel('Combined Acceleration (m/s²)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

