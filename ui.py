# ui.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from data_handler import load_data, process_data
from visualization import plot_data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Particles's colisions")
        self.setGeometry(100, 100, 300, 200)
        
        # Button to charge data
        self.load_button = QPushButton("Charge data", self)
        self.load_button.clicked.connect(self.load_data)
        self.load_button.resize(200, 50)
        self.load_button.move(50, 30)
        
        # Button to charge visualization
        self.plot_button = QPushButton("Show visualization", self)
        self.plot_button.clicked.connect(self.show_plot)
        self.plot_button.resize(200, 50)
        self.plot_button.move(50, 100)
        
        # Charge data
        self.data = None
    
    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.data = load_data(file_path)
            self.data = process_data(self.data)
            print("Data charged and processed correctly.")
    
    def show_plot(self):
        if self.data is not None:
            plot_data(self.data)
        else:
            print("The data hasn´t been charged yet.")

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

