# -*- coding: utf-8 -*-
import numpy as np
import serial
import time
import matplotlib.pyplot as plt
czas=[]
count=0
z1baudrate = 115200
z1port = 'COM3'  # set the correct port before run it
fkontener=np.array([])
zkontener=[]
z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2  # set read timeout
# print z1serial  # debug serial.
print(z1serial.is_open)  # True for opened
if z1serial.is_open:
    while True:
        size = z1serial.inWaiting()
        if size>=22:
            data = z1serial.read(11)
            fkontener=np.append(fkontener,float(data))
            czas.append(time.time())
            print(data)
            print(count)
            count=count+1
            data = z1serial.read(11)
            print(data)
            zkontener.append(float(data))
            if count>1999:
                if np.sum(fkontener[np.size(fkontener)-1000:np.size(fkontener)-1])-np.sum(fkontener[np.size(fkontener)-2000:np.size(fkontener)-1001])<10:
                    break
            #if float(data)>38.5:
             #   break
fczas=[]
for x in czas:
    fczas=np.append(fczas,float(x))
fczas=fczas-fczas[0]*np.ones(np.size(fczas))
plt.plot(fczas,fkontener)

def derivative(time,function):
    lgt=len(time)
    return (time[0:lgt-2],(function[1:lgt-1]-function[0:lgt-2])/(time[1:lgt-1]-time[0:lgt-2]))
tim,der=derivative(fczas,fkontener)
plt.figure()
plt.plot(tim,der)
plt.figure()
plt.plot(fczas[0:int(len(czas)/16)],fkontener[0:int(len(czas)/16)])
count=0
suma=0
mean=np.array([])
meanczas=np.array([])
start=fczas[0]
for index,x in enumerate(fkontener):
    suma=suma+x
    count=count+1
    if count==1000:
        mean=np.append(mean,suma/1000)
        meanczas=np.append(meanczas,(fczas[index]+start)/2)
        start=fczas[index]
        suma=0
        count=0
meanderczas,meander=derivative(meanczas,mean)
plt.figure()
plt.plot(meanderczas,meander)
timedelay=meanderczas[np.argmax(meander)]
szukane=(np.max(fkontener)-fkontener[0])*(1-np.exp(-1))+fkontener[0]
znalezione=0
znalezioneindex=0
for index,x in enumerate(fkontener):
    if abs(x-szukane)<abs(znalezione-szukane):
        znalezione=x
        znalezioneindex=index
timeconstant=fczas[znalezioneindex]-timedelay
k=np.argmax(meander)/65536
nsyg=np.array([])
xp=0
for x in fkontener:
    xp=np.exp(-np.pi/4)*xp+(1-np.exp(-np.pi/4))*x
    nsyg=np.append(nsyg,xp)
plt.figure()
plt.plot(fczas,nsyg)
tim,der=derivative(fczas,nsyg)
plt.figure()
plt.plot(tim,der)
plt.figure()
plt.plot(tim[100:np.size(tim)],der[100:np.size(tim)])
z1serial.close()

        


