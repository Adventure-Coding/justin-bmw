"""Script to plot data"""

"""
DONT FORGET TO INSTALL PANDAS & MATPLOTLIB

pip3 install pandas
pip3 install matplotlib

"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Plot data
# Place path to your data
df = pd.read_csv("./3-merged-bmw.csv")


plot_airgo = "left_leg_inclination"
plot_bmw = "Left Hip Flexion/Extension"

timestamps = df['timestamp']
airgo_data = df[plot_airgo]
bmw_data = df[plot_bmw]

# Step 4: Plot the data
plt.figure(figsize=(14, 8))

# Plot neck_flection
plt.plot(timestamps, airgo_data, label=plot_airgo, color='b')

# Plot head_flexion_extension
plt.plot(timestamps, bmw_data, label=plot_bmw, color='r')

# Adding labels, title, and legend
plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.title(f'{plot_airgo} and {plot_bmw} Over Time')
plt.legend(loc='best')
plt.grid(True)
plt.xticks(rotation=45)


ax = plt.gca()

# Adjust the number of ticks on the x-axis
ax.xaxis.set_major_locator(MaxNLocator(nbins=20))
# Show the plot
plt.show()

# Calculate common parameters
mean_signal1 = round(airgo_data.mean(), 2)
mean_signal2 = round(bmw_data.mean(), 2)

std_signal1 = round(airgo_data.std(), 2)
std_signal2 = round(bmw_data.std(), 2)

variance_signal1 = round(airgo_data.var(), 2)
variance_signal2 = round(bmw_data.var(), 2)

correlation, _ = pearsonr(airgo_data, bmw_data)
correlation = round(correlation, 2)

rmse = round(np.sqrt(mean_squared_error(airgo_data, bmw_data)), 2)
mae = round(mean_absolute_error(airgo_data, bmw_data), 2)
max_error = round(np.max(np.abs(airgo_data - bmw_data)), 2)

# Print the results
print(f"Mean Airgonomics: {mean_signal1}")
print(f"Mean xsense: {mean_signal2}")
print(f"Correlation Coefficient: {correlation}")
print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
print(f"Max Error: {max_error}")
