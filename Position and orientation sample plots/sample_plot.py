import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
 
def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)
     
    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)
     
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)
     
    return roll_x, pitch_y, yaw_z # in radians

def main():
    # Read CSV file
    data = pd.read_csv("sample_movement_data.csv")

    # Extract orientation and position data
    orientation_w = data["HeadOrientationW"]
    orientation_x = data["HeadOrientationX"]
    orientation_y = data["HeadOrientationY"]
    orientation_z = data["HeadOrientationZ"]
    position_x = data["HeadPosX"]
    position_y = data["HeadPosY"]
    position_z = data["HeadPosZ"]
    time = data["time"]

    # Convert from quaternions to euler angles
    roll = []
    pitch = []
    yaw = []
    for i in range(len(orientation_w)):
        roll_temp, pitch_temp, yaw_temp = euler_from_quaternion(orientation_z[i], orientation_x[i], orientation_y[i], orientation_w[i])
        roll.append(np.rad2deg(roll_temp))
        pitch.append(np.rad2deg(pitch_temp))
        yaw.append(np.rad2deg(yaw_temp))

    # Plot the figures
    plt.figure()
    plt.ylabel('Rotation angles [deg]')
    plt.xlabel('Time [s]')
    plt.plot(time, roll)
    plt.plot(time, pitch)
    plt.plot(time, yaw)
    plt.legend(['roll', 'pitch', 'yaw'])

    plt.figure()
    plt.ylabel('Position [m]')
    plt.xlabel('Time [s]')
    plt.plot(time, position_z)
    plt.plot(time, position_x)
    plt.plot(time, position_y)
    plt.legend(['z', 'x', 'y'])

    plt.show()

if __name__ == '__main__':
    main()
