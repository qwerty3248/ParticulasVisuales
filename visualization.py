# visualization.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_data(data):
    """
    Show the data in a 3D grafic.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Look at the particles in 3D
    scatter = ax.scatter(data['x'], data['y'], data['z'], 
                         c=data['energy_norm'], cmap='cool', s=data['velocity_norm']*100)
    
    # Labels and titles 
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.colorbar(scatter, label='Normalize energy')
    
    plt.show()

