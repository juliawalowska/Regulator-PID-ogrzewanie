# -*- coding: utf-8 -*-
import numpy as np
import serial
import time
import matplotlib.pyplot as plt
import keyboard
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
saved=time.time()
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
            zkontener=np.append(zkontener,float(data))
            if abs(time.time()-saved)>1:
                plt.clf()
                plt.plot(czas,f1kontener);
                plt.plot(czas,zkontener,'g')
                plt.plot(czas,zkontener*1.01,'r')
                plt.plot(czas,zkontener*0.99,'r')
                plt.legend(["aktualna","zadana","zadana+-1%"])
                plt.title("BMP280 logger")
                plt.xlabel("Time (s)")
                plt.ylabel("Temperature (C)")
                plt.show()
                plt.pause(0.0001)
                saved=time.time()
            if keyboard.is_pressed("s"):
                break
            #if float(data)>38.5:
             #   break
plt.figure()
f1czas=[]
for x in czas:
    f1czas=np.append(f1czas,float(x))
f1czas=f1czas-f1czas[0]*np.ones(np.size(f1czas))
plt.plot(f1czas,f1kontener)
z1serial.close()
plt.figure()
plt.clf()
plt.plot(f1czas,f1kontener);
plt.plot(f1czas,zkontener,'g')
plt.plot(f1czas,zkontener*1.01,'r')
plt.plot(f1czas,zkontener*0.99,'r')
plt.legend(["aktualna","zadana","zadana+-1%"])
plt.title("BMP280 logger")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.show()