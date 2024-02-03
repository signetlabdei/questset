import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This script plots:
# 1) the heatmap of the HMD position in the XZ plane from time_i to time_f 
# 2) the HMD elevation over time from time_i to time_f
# 3) the joystick elevation over time from time_i to time_f

time_i = 0  # initial time [s]
time_f = 300  # final time [s]

def main():
    # Load csv
    df = pd.read_csv("sample_movement_data.csv", dtype={"HeadPosX": float, "HeadPosY": float, "HeadPosZ": float, "RightTouchPosY": float, "time": float})

    # Filter the time interval
    df = df[(df['time'] >= time_i) & (df['time'] <= time_f)]

    # Plot the heatmap of the HMD position in the XZ plane
    sns.kdeplot(x=df['HeadPosX'], y=df['HeadPosZ'], fill=True, n_levels=5)
    plt.title("HMD Position in the XZ Plane")
    plt.xlabel("Axis X [m]")
    plt.ylabel("Axis Z [m]")
    plt.grid(True)
    plt.show()

    # Plot the HMD elevation over time
    plt.title("HMD Elevation Over Time")
    plt.plot(df['time'], df['HeadPosY'])
    plt.xlabel("Time [s]")
    plt.ylabel("HMD Elevation [m]")
    plt.grid(True)
    plt.show()

    # Plot the joystick elevation over time
    plt.title("Joystick Elevation Over Time")
    plt.plot(df['time'], df['RightTouchPosY'])
    plt.xlabel("Time [s]")
    plt.ylabel("Joystick Elevation [m]")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()