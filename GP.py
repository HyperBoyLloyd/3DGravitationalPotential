import numpy as np
from mayavi import mlab

# User defined variables
x = (-10, 10, 100)
y = (-10, 10, 100)
z = (-10, 10, 100)
num_points = 2
mass_range = (-2, 2)
contours = 100
opacity = 0.2
nb_labels = 5
colorbar_title = 'Gravitational Potential'
title = 'Gravitational Potential'
title_height = 0.9

def gravitational_potential(x, y, z):
    # Calculate the gravitational potential using a function that warps the plane
    potential = np.zeros(x.shape)
    for i in range(num_points):
        # Generate a random point mass
        mass_x, mass_y, mass_z = np.random.uniform(*mass_range, size=3)
        mass = np.random.uniform(*mass_range)

        # Calculate the distance from the point mass to each point in the grid
        r = np.sqrt((x - mass_x) ** 2 + (y - mass_y) ** 2 + (z - mass_z) ** 2)

        # Calculate the gravitational potential at each point in the grid
        potential -= mass / r

    return potential

# Create a meshgrid of points in 3D space
x_arr = np.linspace(*x)
y_arr = np.linspace(*y)
z_arr = np.linspace(*z)
x, y, z = np.meshgrid(x_arr, y_arr, z_arr, indexing='ij')
potential = gravitational_potential(x, y, z)

# Create a 3D mesh plot of the potential
src = mlab.pipeline.scalar_field(x, y, z, potential)
surface = mlab.pipeline.iso_surface(src, contours=contours, colormap='plasma', opacity=opacity)
surface.actor.property.specular = 0

# Add grid lines to the plot
mlab.outline()
mlab.axes(xlabel='X', ylabel='Y', zlabel='Z', nb_labels=nb_labels)

# Add a color bar to the plot
mlab.colorbar(title=colorbar_title, orientation='vertical', nb_labels=nb_labels)

# Add a title to the plot
mlab.title(title, height=title_height)

# Display the plot
mlab.show()
