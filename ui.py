# ui.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from data_handler import load_data, process_data
from visualization import plot_data

class MainWindow(QMainWindow):
    """
    Main application window for particle collision visualization.
    
    This class creates the GUI and manages user interactions for loading data
    and displaying visualizations.
    """
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Particles' Collisions")  # Set the window title
        self.setGeometry(100, 100, 300, 200)  # Set the window size
        
        # Button to load data
        self.load_button = QPushButton("Load data", self)
        self.load_button.clicked.connect(self.load_data)
        self.load_button.resize(200, 50)
        self.load_button.move(50, 30)
        
        # Button to show visualization
        self.plot_button = QPushButton("Show visualization", self)
        self.plot_button.clicked.connect(self.show_plot)
        self.plot_button.resize(200, 50)
        self.plot_button.move(50, 100)
        
        self.data = None  # Placeholder for loaded data
    
    def load_data(self):
        """
        Load data from a selected CSV file.
        
        This function opens a file dialog for the user to select a CSV file,
        loads the data, processes it, and stores it for later visualization.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV file", "", "CSV Files (*.csv)")
        if file_path:
            self.data = load_data(file_path)  # Load the data using the load_data function
            self.data = process_data(self.data)  # Process the data for visualization
            print("Data loaded and processed successfully.")
    
    def show_plot(self):
        """
        Display the visualization of the loaded data.
        
        This function checks if data has been loaded and calls the plotting function
        to visualize the particle collisions.
        """
        if self.data is not None:
            plot_data(self.data)  # Call the function to plot data
        else:
            print("Data has not been loaded yet.")  # Inform the user that no data is available

def run():
    """
    Run the application.
    
    This function initializes the QApplication and displays the main window.
    """
    app = QApplication(sys.argv)  # Create a QApplication instance
    window = MainWindow()  # Create the main window
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Execute the application

