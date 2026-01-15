import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Theoretical prob function
def theoretical_prob(n):
    return 1 - np.exp(-n*(n-1)/(2*365))

# Data
n_people = np.arange(1, 101)
probs = theoretical_prob(n_people)

# Set up figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 1)
ax.set_title('Birthday Paradox Probability Curve', fontsize=16)
ax.set_xlabel('Number of People', fontsize=14)
ax.set_ylabel('Probability of Shared Birthday', fontsize=14)
ax.grid(True)
ax.axhline(y=0.5, color='r', linestyle='--')
ax.axvline(x=23, color='r', linestyle='--')
ax.text(25, 0.52, '50% at ~23 people', fontsize=12)

# Line for animation
line, = ax.plot([], [], 'b-', linewidth=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(n_people[:frame], probs[:frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(n_people), init_func=init, interval=100, blit=True)

plt.show()  # Or ani.save('birthday_curve.gif', writer='pillow') for GIF