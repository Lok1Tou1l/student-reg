import cv2 as cv
import database as db

def capture_picture():
    cap = cv.VideoCapture(0)
    ret, frame = cap.read()
    if ret :
        cv.imshow('Captured Image', frame)
        cv.waitKey(0)
        cv.destroyAllWindows()


        ret, buffer = cv.imencode('.jpg', frame)
        img_blob = buffer.tobytes()

        db.save_to_database(name,email, phone, specialty, img_blob)
    cap.release()

