# Define the linear trajectory as a list of points
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new list of points with a curved path for the first two points
curved_trajectory = [
  [0.0,0.0,0.0],
  [0.0, 0.0, 1.5],
  [0.0, 1.0, 1.5],
  [0.0, 2.0, 1.5],
  [1.0, 2.0, 1.5],
  [2.0, 2.0, 1.5],
  [2.0,1.7,1.5],
  [2.0,2.0,1.5],
  [1.7,2.0,1.5],
  [1.7,1.7,1.5],
  [1.7,1.7,1.5],
  [1.0,1.0,1.5],
  [0.0,0.0,1.5],
  [0.0,0.0,0.0]
]

# Convert the list of curved points into separate x, y, and z arrays
x_curved, y_curved, z_curved = zip(*curved_trajectory)

# Compute a cubic spline interpolation of the x, y, and z coordinates
cs_x = CubicSpline(np.arange(len(x_curved)), x_curved)
cs_y = CubicSpline(np.arange(len(y_curved)), y_curved)
cs_z = CubicSpline(np.arange(len(z_curved)), z_curved)

# Evaluate the spline functions at 1000 evenly spaced points
n_eval = 700
x_eval = cs_x(np.linspace(0, len(x_curved) - 1, n_eval))
y_eval = cs_y(np.linspace(0, len(y_curved) - 1, n_eval))
z_eval = cs_z(np.linspace(0, len(z_curved) - 1, n_eval))

# Save the x, y, and z arrays into a text file
data = np.column_stack((x_eval, y_eval, z_eval))
np.savetxt('trajPoints.txt', data, delimiter=' ')

print('Trajectory points saved to trajPoints.txt')

# Create a 3D figure and axis object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the interpolated trajectory as a line
ax.plot(x_eval, y_eval, z_eval, '-')

# Set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Object Tracking Drone Smoothened Trajectory')

# Show the plot
plt.show()
