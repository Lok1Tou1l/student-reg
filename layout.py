from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QApplication
import cv2 as cv
import database as db

class StudentRegistration(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Registration')
        self.setGeometry(1270,1270,720,720)

        self.name_label = QLabel('Name')
        self.name_input = QLineEdit()

        self.email_label = QLabel('Email')
        self.email_input = QLineEdit()

        self.phone_label = QLabel('Phone')
        self.phone_input = QLineEdit()

        self.specialty_label = QLabel('Specialty')
        self.dropdown = QComboBox()
        self.dropdown.addItems(['Mobile Development', 'Web Development', 'AI', 'Cyber Security','Game Development','UI/UX Design','Graphics Design'])

        self.capture_button = QPushButton('Capture Picture')
        self.capture_button.clicked.connect(self.capture_picture)  # Fixed the method name

        self.register_button = QPushButton('Register')
        self.register_button.clicked.connect(self.submit_form)
        

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.specialty_label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.capture_button)
        layout.addWidget(self.register_button)


        self.setLayout(layout)
    def submit_form (self,name,email,phone,specialty,image):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        specialty = self.dropdown.currentText()
        image = self.capture_picture()
        db.save_to_database(name,email,phone,specialty,image)

    
    def capture_picture(self):  # Added self parameter
        cap = cv.VideoCapture(0)
        ret, frame = cap.read()
        if ret :
            cv.imshow('Captured Image', frame)
            cv.waitKey(0)
            cv.destroyAllWindows()

            ret, buffer = cv.imencode('.jpg', frame)
            img_blob = buffer.tobytes()

        cap.release()


app = QApplication([])
window = StudentRegistration()
window.show()
app.exec_()


