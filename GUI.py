import numpy as np
import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Serial port setup
z1baudrate = 115200
z1port = 'COM3'  # set the correct port before run it
z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2  # set read timeout
print(z1serial.is_open)  # True for opened

# Initialize containers for data
f1kontener = np.array([])
czas = []
zkontener = []

# Plot setup
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 5)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    size = z1serial.inWaiting()
    if size >= 22:
        data = z1serial.read(11)
        f1kontener = np.append(f1kontener, float(data))
        czas.append(time.time())
        print(data)

        # Update plot data
        xdata.append(time.time() - czas[0])
        ydata.append(float(data))
        ln.set_data(xdata, ydata)
        ax.set_xlim(left=max(0, xdata[-1]-5), right=xdata[-1]+1)
        ax.set_ylim(min(ydata)-1, max(ydata)+1)

    return ln,

# Create animation
ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=50, cache_frame_data=False)

plt.show()
