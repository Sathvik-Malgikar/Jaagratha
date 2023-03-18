from flask import Flask, Response

import cv2
from time import sleep
import socket


vid1 = cv2.VideoCapture("http://192.168.137.128:4747/video?640x480")
def gen_frames():  
    while True:
        success, frame = vid1.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            cv2.imshow("test", frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 


app = Flask(__name__)

@app.route('/auth')
def home():
    return 'Hello, World!'

@app.route('/feed')
def videofeed1():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    



if __name__ == '__main__':
    app.run()