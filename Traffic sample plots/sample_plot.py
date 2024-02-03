import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Read CSV file
    data = pd.read_csv("sample_traffic_data.csv",
                       dtype={"size":float,
                              "time":float,
                              "direction":str})

    # remove the header size from the packet size
    header_size = 27  # USBPCAP pseudo-header
    data["size"] = data["size"] - header_size

    # %% plot the size of the packets over time
    window_l = 1  # define a time window [s] for the plotting

    sns.scatterplot(data=data, x="time", y="size", hue="direction")
    plt.xlabel("Time [s]")
    plt.ylabel("Packet size [B]")
    plt.xlim([0,window_l])
    plt.grid()
    plt.show()

    # # filter only downlink (DL) packets that are larger than 5 KB
    data_dl = data[(data["direction"] == "DL") & (data["size"] > 5e3)]
    sns.scatterplot(data=data_dl, x="time", y="size")
    plt.xlabel("Time [s]")
    plt.ylabel("Packet size [B]")
    plt.xlim([0,window_l])
    plt.ylim([4e4,7e4])
    plt.grid()
    plt.show()

    # compute the Inter Packet Inter-arrival time
    time = data_dl["time"].values
    ipi = np.diff(time,1)
    
    # plot the histogram
    sns.histplot(data=ipi*1e3,stat="density")
    plt.xlabel("IPI [ms]")
    plt.ylabel("Density")
    plt.grid()
    plt.show()

    # zoom in
    sns.histplot(data=ipi*1e3, stat="density")
    plt.xlabel("IPI [ms]")
    plt.ylabel("Density")
    plt.xlim([0,20])
    plt.grid()
    plt.show()


if __name__=='__main__':
     main()
