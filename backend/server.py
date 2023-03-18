from flask import Flask, Response, request
from flask_cors import CORS
import cv2
from time import sleep
import socket
import json
import pymongo


vid1 = cv2.VideoCapture("http://192.168.137.128:4747/video?640x480")
def gen_frames():  
    while True:
        success, frame = vid1.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 


app = Flask(__name__)
CORS(app)

def auth(data):
    import pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017")
    auth_db = client["Jaagrutha"]
    user_pass = auth_db["Auth"]
    queryResult = user_pass.find(data)
    for x in queryResult:
        return "1"
    return "0"

@app.route('/auth', methods=["GET", "POST"])
def home():
    print(json.loads(request.data))
    return auth(json.loads(request.data))


@app.route('/feed', methods=["POST", "GET"])
def videofeed1():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    

if __name__ == '__main__':
    app.run()