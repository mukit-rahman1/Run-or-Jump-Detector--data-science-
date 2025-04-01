import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('normalized_features.csv')

# Parameters
person = 'mukit'
window_duration = 5  # seconds

# Filter walking and jumping
walk = df[(df['person'] == person) & (df['activity'] == 'walking')]
jump = df[(df['person'] == person) & (df['activity'] == 'jumping')]

# Time axes
time_walk = np.arange(len(walk)) * window_duration
time_jump = np.arange(len(jump)) * window_duration

# Plot
plt.figure(figsize=(10, 5))
plt.plot(time_walk, walk['absolute_mean'], label='Walking', color='b')
plt.plot(time_jump, jump['absolute_mean'], label='Jumping', color='r')
plt.title(f'{person.capitalize()} - absolute_mean (Walking vs Jumping)')
plt.xlabel('Time (s)')
plt.ylabel('Normalized Mean Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



# Load data
df = pd.read_csv('normalized_features.csv')

# Parameters
person = 'sydney'
window_duration = 5  # seconds

# Filter walking and jumping
walk = df[(df['person'] == person) & (df['activity'] == 'walking')]
jump = df[(df['person'] == person) & (df['activity'] == 'jumping')]

# Time axes
time_walk = np.arange(len(walk)) * window_duration
time_jump = np.arange(len(jump)) * window_duration

# Plot
plt.figure(figsize=(10, 5))
plt.plot(time_walk, walk['absolute_mean'], label='Walking', color='b')
plt.plot(time_jump, jump['absolute_mean'], label='Jumping', color='r')
plt.title(f'{person.capitalize()} - absolute_mean (Walking vs Jumping)')
plt.xlabel('Time (s)')
plt.ylabel('Normalized Mean Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



# Load data
df = pd.read_csv('normalized_features.csv')

# Parameters
person = 'tyler'
window_duration = 5  # seconds

# Filter walking and jumping
walk = df[(df['person'] == person) & (df['activity'] == 'walking')]
jump = df[(df['person'] == person) & (df['activity'] == 'jumping')]

# Time axes
time_walk = np.arange(len(walk)) * window_duration
time_jump = np.arange(len(jump)) * window_duration

# Plot
plt.figure(figsize=(10, 5))
plt.plot(time_walk, walk['absolute_mean'], label='Walking', color='b')
plt.plot(time_jump, jump['absolute_mean'], label='Jumping', color='r')
plt.title(f'{person.capitalize()} - absolute_mean (Walking vs Jumping)')
plt.xlabel('Time (s)')
plt.ylabel('Normalized Mean Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()