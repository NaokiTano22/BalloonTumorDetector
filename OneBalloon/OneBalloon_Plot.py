#Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import OneBalloon_CreateArray as ca

#Acquire datasets from csv files
CylEco = ca.CreateArray('OneBalloon_data\CylEco1106.csv')
CylDS10 = ca.CreateArray('OneBalloon_data\CylDS100615.csv')
CylDS30 = ca.CreateArray('OneBalloon_data\CylDS300530.csv')
HemEco = ca.CreateArray('OneBalloon_data\HemEco1110.csv')
ConeEco = ca.CreateArray('OneBalloon_data\PyEco1106.csv')

cm = 1/2.54     #centimeters in inches
n = 9.807/1000

font = {'family' : 'Times New Roman', 'size'   : 10.5}
plt.rc('font', **font)

##################################################
##  One Balloon in different material
##      Depth - Loading Force
##################################################

plt.subplots(figsize=(12*cm, 10*cm))

plt.errorbar(CylEco[:9,0], (CylEco[:9,3]-CylEco[0,3])*n, yerr=CylEco[:9,4]*n,
              lw=1.5, marker="o", markersize=1, elinewidth=0.75, capsize=1, color="tab:blue", zorder=3, label='Eco')
plt.errorbar(CylDS10[:9,0], (CylDS10[:9,3]-CylDS10[0,3])*n, yerr=CylDS10[:9,4]*n,
              lw=1.5, marker="o", markersize=1, elinewidth=0.75, capsize=1, color="tab:orange", label='DS10')
plt.errorbar(CylDS30[:9,0], (CylDS30[:9,3]-CylDS30[0,3])*n, yerr=CylDS30[:9,4]*n,
              lw=1.5, marker="o", markersize=1, elinewidth=0.75, capsize=1, color="tab:green", label='DS30')
plt.plot([0,4], [3.2,3.2], color='k', zorder=4, linestyle='dashed', lw=1.5)

plt.legend()
plt.xlabel('Indented Depth [mm]')
plt.ylabel('Loading Force [N]')

plt.show()

##################################################
##  One Balloon in different material
##      Depth - Internal Pressure
##################################################

plt.subplots(figsize=(12*cm, 10*cm))

plt.errorbar(CylEco[:,0], CylEco[:,1],lw=1.5, color='tab:blue', yerr=CylEco[:,2],
              zorder=3, markersize=1, elinewidth=0.75, capsize=1, label='Cylinder')
plt.errorbar(HemEco[:,0], HemEco[:,1],lw=1.5, color='tab:orange', yerr=HemEco[:,2],
              markersize=1, elinewidth=0.75, capsize=1, label='Hemisphere')
plt.errorbar(ConeEco[:,0], ConeEco[:,1],lw=1.5, color='tab:green', yerr=ConeEco[:,2],
              markersize=1, elinewidth=0.75, capsize=1, label='Cone')

plt.legend()
plt.xlabel('Indented Depth [mm]')
plt.ylabel('Internal Pressure [kPa]')

plt.show()

##################################################
##  One Balloon in different material
##      Depth - Loading Force
##################################################

plt.subplots(figsize=(12*cm, 10*cm))

plt.errorbar(CylEco[:9,0], (CylEco[:9,3]-CylEco[0,3])*n, yerr=CylEco[:9,4]*n,
              lw=1.5, marker="o", markersize=1, elinewidth=0.75, capsize=1, color="tab:blue", zorder=3, label='Cylinder')
plt.errorbar(HemEco[:9,0], (HemEco[:9,3]-HemEco[0,3])*n, yerr=HemEco[:9,4]*n,
              lw=1.5, marker="o", markersize=1, elinewidth=0.75, capsize=1, color="tab:orange", label='Hemisphere')
plt.errorbar(ConeEco[:9,0], (ConeEco[:9,3]-ConeEco[0,3])*n, yerr=ConeEco[:9,4]*n,
              lw=1.5, marker="o", markersize=1, elinewidth=0.75, capsize=1, color="tab:green", label='Cone')
plt.plot([0,4], [3.2,3.2], color='k', zorder=4, linestyle='dashed', lw=1.5)

plt.legend()
plt.xlabel('Indented Depth [mm]')
plt.ylabel('Loading Force [N]')

plt.show()