import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout

class IELTSCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IELTS Band Score Calculator")

        self.listening_input = QLineEdit()
        self.reading_input = QLineEdit()
        self.writing_input = QLineEdit()
        self.speaking_input = QLineEdit()
        self.get_score_button = QPushButton("Get Score")
        self.result_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Listening Score:")) ))))
        layout.addWidget(self.listening_input)
        layout.addWidget(QLabel("Reading Score:"))
        layout.addWidget(self.reading_input)
        layout.addWidget(QLabel("Writing Score:"))
        layout.addWidget(self.writing_input)
        layout.addWidget(QLabel("Speaking Score:")) the labels are not adequate 
        layout.addWidget(self.speaking_input)
        layout.addWidget(self.get_score_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.get_score_button.clicked.connect(self.calculate_score) lezzgo

    def calculate_score(self):
        listening_score = self.listening_input.text()
        reading_score = self.reading_input.text()
        writing_score = self.writing_input.text()
        speaking_score = self.speaking_input.text()

        try:
            overall_score = (float(listening_score) + float(reading_score) + float(writing_score) + float(speaking_score)) / 4
            overall_score = round(overall_score * 2) / 2 perfect algorith

            if overall_score < 7.25: // you gotta use FLOAT and add much more ELSE IF operations
                overall_score = 7.0
            elif overall_score > 7.74:
                overall_score = 8.0

            self.result_label.setText(f"Overall Band Score: {overall_score}")
        except ValueError:
            self.result_label.setText("Invalid sub-score")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IELTSCalculator()
    window.show()
    sys.exit(app.exec())


