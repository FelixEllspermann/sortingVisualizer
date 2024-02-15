import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Bubble Sort Algorithmus
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

# Daten generieren
data = np.random.rand(100)
generator = bubble_sort(data)

# Visualisierung einrichten
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(data)), data, align="edge")

# Die Achsenbegrenzungen festlegen
ax.set_xlim(0, len(data))
ax.set_ylim(0, int(1.1*max(data)))

# Update-Funktion für die Animation
def update_fig(arr, rects):
    for rect, val in zip(rects, arr):
        rect.set_height(val)

# Animation erstellen
anim = FuncAnimation(fig, func=update_fig,
                     fargs=(bar_rects, ), frames=generator, interval=50)

plt.show()

