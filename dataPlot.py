

#Lavet af Benjamin: #s214590

import matplotlib.pyplot as plt
import numpy as np

def dataPlot(data):
    """
    Parameters
    __________
    data : N x 3 - Matrix

    Returns:
    --------
    None (displays plots)
    """

    labels = np.array(["Salonella\nEnterica","Bascillus Cereus",
                        "Listeria","Brochothrix\nThermosphacta"])

    rows1, col1 = np.shape(data[data[:, 2] == 1])
    rows2, col2 = np.shape(data[data[:, 2] == 2])
    rows3, col3 = np.shape(data[data[:, 2] == 3])
    rows4, col4 = np.shape(data[data[:, 2] == 4])
    count = np.array([rows1, rows2, rows3, rows4])
    #plt.subplot(2,1,1)
    plt.bar(labels, count)
    plt.ylabel("Count")
    plt.title("Number of Bacteria")
    plt.show()


    #.....................
    x1 = np.sort(data[data[:,2]==1][:,0])
    x2 = np.sort(data[data[:,2]==2][:,0])
    x3 = np.sort(data[data[:,2]==3][:,0])
    x4 = np.sort(data[data[:,2]==4][:,0])

    y1 = np.sort(data[data[:,2]==1][:,1])
    y2 = np.sort(data[data[:,2]==2][:,1])
    y3 = np.sort(data[data[:,2]==3][:,1])
    y4 = np.sort(data[data[:,2]==4][:,1])
    #plt.subplot(2,1,2)
    plt.title("Growth Rate by Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.xlim([10, 60])
    plt.ylim(0, 1)
    plt.plot(x1, y1, color="r", label="Salmonella enterica")
    plt.plot(x2, y2, color="b", label="Bacillus cereus")
    plt.plot(x3, y3, color="g", label="Listeria")
    plt.plot(x4, y4, color="y", label="Brochothrix thermosphacta")
    plt.legend(loc="upper left")
    plt.show()


