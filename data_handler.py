# data_handler.py
import pandas as pd

def load_data(file_path):
    """
    Charge the data from CSV file.
    Each row represens a colision of a particula.
    """
    data = pd.read_csv(file_path)
    # I supposed that CSV has x,y,z,energy,velocity
    # We have to ensure that the file contains the necessary colums to the visualization
    if not {'x', 'y', 'z', 'energy', 'velocity'}.issubset(data.columns):
        raise ValueError("El archivo debe contener las columnas 'x', 'y', 'z', 'energy', 'velocity'")
    
    return data

def process_data(data):
    """
    Process the data, for example, normalize the values of energy and velocity to the visualization.
    """
    # Normalize energy and velocity to be between 0 and 1
    
    data['energy_norm'] = data['energy'] / data['energy'].max()
    data['velocity_norm'] = data['velocity'] / data['velocity'].max()
    
    return data

