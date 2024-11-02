# data_handler.py
import pandas as pd

def load_data(file_path):
    """
    Load the data from a CSV file.
    
    This function reads a CSV file containing particle collision data and ensures
    that the necessary columns ('x', 'y', 'z', 'energy', 'velocity') are present.

    :param file_path: The path to the CSV file to be loaded.
    :return: A pandas DataFrame containing the loaded data.
    :raises ValueError: If the required columns are not found in the CSV file.
    """
    data = pd.read_csv(file_path)
    
    # Check if the required columns are present in the DataFrame
    if not {'x', 'y', 'z', 'energy', 'velocity'}.issubset(data.columns):
        raise ValueError("The file must contain the columns 'x', 'y', 'z', 'energy', 'velocity'")
    
    return data

def process_data(data):
    """
    Process the particle data for visualization.

    This function normalizes the 'energy' and 'velocity' columns of the DataFrame
    to values between 0 and 1 for better visualization.

    :param data: A pandas DataFrame containing particle data.
    :return: The modified DataFrame with normalized 'energy' and 'velocity'.
    """
    # Normalize energy and velocity to be between 0 and 1
    data['energy_norm'] = data['energy'] / data['energy'].max()
    data['velocity_norm'] = data['velocity'] / data['velocity'].max()
    
    return data

