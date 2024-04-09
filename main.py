# Push-Up Tracker
# Author: S. Chu
# Date: 2024-04-08
# Reference: N/A

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QTabWidget, QTableWidget, QTableWidgetItem
from datetime import datetime

class PushupTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pushup Tracker")
        self.setGeometry(100, 100, 850, 250)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.pushup_count_label = QLabel("Pushups: 0")
        self.layout.addWidget(self.pushup_count_label)

        self.pushup_input = QLineEdit()
        self.layout.addWidget(self.pushup_input)

        self.add_pushup_button = QPushButton("Add Pushup")
        self.add_pushup_button.clicked.connect(self.add_pushup)
        self.layout.addWidget(self.add_pushup_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_pushups)
        self.layout.addWidget(self.reset_button)

        self.pushup_counts = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
        self.total_score_label = QLabel("Total Score: 0")
        self.layout.addWidget(self.total_score_label)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.create_pushup_table()

        self.pushup_count = 0

    def add_pushup(self):
        try:
            count = int(self.pushup_input.text())
            day_of_week = self.get_day_of_week()
            self.pushup_counts[day_of_week] += count
            self.pushup_count += count
            self.update_pushup_count_label()
            self.update_total_score_label()
            self.update_pushup_table()
            self.pushup_input.clear()
        except ValueError:
            pass

    def reset_pushups(self):
        self.pushup_counts = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
        self.pushup_count = 0
        self.update_pushup_count_label()
        self.update_total_score_label()
        self.update_pushup_table()

    def update_pushup_count_label(self):
        self.pushup_count_label.setText(f"Pushups: {self.pushup_count}")

    def update_total_score_label(self):
        total_score = sum(self.pushup_counts.values())
        self.total_score_label.setText(f"Total Score: {total_score}")

    def create_pushup_table(self):
        column_headers = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Total']
        self.pushup_table = QTableWidget(1, len(column_headers))  # Adjusted row count
        self.pushup_table.setHorizontalHeaderLabels(column_headers)
        self.tab_widget.addTab(self.pushup_table, "Pushup Count")

    def update_pushup_table(self):
        for i, (day, count) in enumerate(self.pushup_counts.items()):
            self.pushup_table.setItem(0, i, QTableWidgetItem(str(count)))

        total_pushups = sum(self.pushup_counts.values())
        total_column_index = len(self.pushup_counts)
        self.pushup_table.setItem(0, total_column_index, QTableWidgetItem(str(total_pushups)))

    def get_day_of_week(self):
        return datetime.now().strftime('%A')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PushupTracker()
    window.show()
    sys.exit(app.exec())
