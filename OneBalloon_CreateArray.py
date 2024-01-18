#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib as mpl

#Return Dataset [[depth, ave_pressure, std_pressure, ave_force, std_force][...]...]
def CreateArray(filename):
    #Read datasets
    DataArray = pd.read_csv(filename, header=None)
    Voltage = DataArray.values[:,1]
    MaxForce = DataArray.values[:,2]
    MinForce = DataArray.values[:,3]

    #Eliminate unnecessary data
    DelIndex = np.where(Voltage == 1000000)
    delin = np.arange(DelIndex[0][0])
    delin = np.append(delin, DelIndex[0])

    #Create arrays
    VArray = np.delete(Voltage, delin)
    PArray = (VArray - np.mean(VArray[:50]))*15*6.895*5/4.5/1024
    FmaxArray = np.delete(MaxForce, delin)
    FminArray = np.delete(MinForce, delin)
    DepthArray = []
    for i in np.arange(len(DelIndex[0])):
        if i != 0:
            DepthArray = np.append(DepthArray, np.full(DelIndex[0][i]-DelIndex[0][i-1]-1, 0.5*(i-1)))
    
    index = int(np.shape(DepthArray)[0])
    Dataset = np.zeros([index//50, 5])
    for i in np.arange(index//50):
        temp_p = PArray[i*50:(i+1)*50]
        fmax = FmaxArray[i*50]
        fmin = FminArray[i*50]
        temp = [i*0.5, np.average(temp_p), np.std(temp_p), (fmax+fmin)/2, np.std([fmax, fmin])]
        Dataset[i,:] = temp

    #return datase
    return Dataset


