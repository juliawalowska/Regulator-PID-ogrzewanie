import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import serial
import threading
import time

# Inicjalizacja połączenia szeregowego
ser = serial.Serial('COM3', 115200)  

def read_from_stm():
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').rstrip()
            print(f"Otrzymano dane: {line}")  # Dodano logowanie otrzymanych danych

            try:
                parts = line.split(', ')
                if len(parts) > 0 and ": " in parts[0]:
                    sensor_val_str = parts[0].split(': ')[1]
                    sensor_val = float(sensor_val_str)
                    y_values.append(sensor_val)
                    x_values.append(time.time())
                else:
                    print("Nieprawidłowy format danych")
            except ValueError as e:
                print(f"Błąd podczas parsowania danych: {line}. Szczegóły błędu: {e}")


def reset_plot():
    x_values.clear()
    y_values.clear()
    ax.clear()
    ax.axhline(y=set_point.get(), color='r', linestyle='-', label="Wartość zadana")
    ax.legend()
    canvas.draw()

def update_plot():
    while True:
        time.sleep(0.1)  # Opóźnienie dla zmniejszenia obciążenia procesora

        if len(x_values) == len(y_values) and len(x_values) > 0:
            ax.clear()
            ax.plot(x_values, y_values, label="Czujnik")
            ax.axhline(y=set_point.get(), color='r', linestyle='-', label="Wartość zadana")
            ax.axhline(y=set_point.get() * 1.05, color='g', linestyle='--', label="5% Odchył")
            ax.axhline(y=set_point.get() * 0.95, color='g', linestyle='--')
            ax.legend()
            canvas.draw()

set_point = tk.DoubleVar(value=4)
root = tk.Tk()
root.title("Temperature Regulator")  # Tytuł okna

fig, ax = plt.subplots()
ax.set_title("Temperature Regulator")  # Tytuł wykresu
canvas = FigureCanvasTkAgg(fig, master=root)
widget = canvas.get_tk_widget()
widget.grid(row=0, column=0, columnspan=4)

x_values = []
y_values = []

# Uruchomienie wątków
threading.Thread(target=read_from_stm, daemon=True).start()
threading.Thread(target=update_plot, daemon=True).start()

root.mainloop()