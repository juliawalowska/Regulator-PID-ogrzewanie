# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 01:17:58 2024

@author: Józef
"""
import numpy as np
import serial
import time
import matplotlib.pyplot as plt
plt.ion()
czas=np.array([])
count=0
z1baudrate = 115200
z1port = 'COM3'  # set the correct port before run it
f1kontener=np.array([])
zkontener=[]
z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2  # set read timeout
# print z1serial  # debug serial.
print(z1serial.is_open)  # True for opened
fig,ax=plt.subplots()
if z1serial.is_open:
    while True:
        size = z1serial.inWaiting()
        if size>=22:
            data = z1serial.read(11)
            f1kontener=np.append(f1kontener,float(data))
            czas=np.append(czas,float(time.time()))
            print(data)
            print(count)
            count=count+1
            data = z1serial.read(11)
            print(data)
            zkontener.append(data)
            plt.clf()
            plt.plot(czas,f1kontener);
            plt.title("BMP280 logger")
            plt.xlabel("Time (s)")
            plt.ylabel("Temperature (C)")
            plt.show()
            plt.pause(0.0001)
            if count>1999:
                if np.sum(f1kontener[np.size(f1kontener)-1000:np.size(f1kontener)-1])-np.sum(f1kontener[np.size(f1kontener)-2000:np.size(f1kontener)-1001])<10:
                    break
            #if float(data)>38.5:
             #   break
f1czas=[]
for x in czas:
    f1czas=np.append(f1czas,float(x))
f1czas=f1czas-f1czas[0]*np.ones(np.size(f1czas))
plt.plot(f1czas,f1kontener)
z1serial.close()