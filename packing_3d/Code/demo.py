import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create a figure and subplots
fig, ax = plt.subplots(3, 1, figsize=(8, 12))

# Plot on the first subplot
ax[0].plot(x, y1, label='sin(x)')
ax[0].set_title('Sine Function')
ax[0].set_xlabel('x')
ax[0].set_ylabel('sin(x)')
ax[0].legend()
plt.pause(1)  # Pause to display the plot

# Plot on the second subplot
ax[1].plot(x, y2, label='cos(x)', color='red')
ax[1].set_title('Cosine Function')
ax[1].set_xlabel('x')
ax[1].set_ylabel('cos(x)')
ax[1].legend()
plt.pause(1)  # Pause to display the plot

# Plot on the third subplot
ax[2].plot(x, y3, label='tan(x)', color='green')
ax[2].set_title('Tangent Function')
ax[2].set_xlabel('x')
ax[2].set_ylabel('tan(x)')
ax[2].legend()
ax[2].set_ylim(-10, 10)  # Limiting y-axis to avoid large values of tan(x)
plt.pause(1)  # Pause to display the plot

# Show the final figure with all subplots
plt.show()
