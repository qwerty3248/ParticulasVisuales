# visualization.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_data(data):
    """
    Visualize the particle data in a 3D plot.
    
    This function creates a 3D scatter plot of the particle collisions,
    using normalized energy for color and normalized velocity for size.

    :param data: A pandas DataFrame containing the particle data.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Create a 3D axis
    
    # Create a scatter plot for the particles in 3D
    scatter = ax.scatter(data['x'], data['y'], data['z'], 
                         c=data['energy_norm'], cmap='cool', s=data['velocity_norm'] * 100)
    
    # Set labels and titles 
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.colorbar(scatter, label='Normalized Energy')  # Add a colorbar for normalized energy
    
    plt.show()  # Display the plot

