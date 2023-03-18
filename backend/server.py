from flask import Flask, Response, request
from flask_cors import CORS
import cv2
from time import sleep
import json
import pymongo
from tensorflow import keras
import tensorflow as tf
import whole
import time
import asyncio

app = Flask(__name__)
CORS(app)

vid1 = cv2.VideoCapture("http://192.168.137.128:4747/video?640x480")
vid2 = cv2.VideoCapture("http://192.168.137.242:4747/video?640x480")
# vid3 = cv2.VideoCapture("http://192.168.137.84:4747/video?640x480")

vidStreams = [vid1, vid2]
vidFeeds = []

crimeDetector = keras.models.load_model("crime_detect_modelH5.h5")



## face recogniser specific stuff
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
names = ['None', 'Pranav', 'Hemabhushan', 'Ilza', 'Z', 'W']
minW = 0.1*vid1.get(3)
minH = 0.1*vid1.get(4)


async def idk(a, b, c, d):
    whole.GRAND(a, b, c, d)
    return None

def genVidFeed(vid):
    prob = 1
    count = 1
    def gen_frames():
        nonlocal count, prob
        timer=time.time()
        while True:
            count += 1
            success, frame = vid.read()  # read the camera frame
            
            if (0):
                frame2 = cv2.resize(frame, (64,64))
                frame2 = tf.expand_dims(frame2, axis=0)
                pred_val = crimeDetector(frame2)
                pred_val = tf.get_static_value(pred_val)[0]

                maxval = max(pred_val)
                #flipped for testing
                if maxval == pred_val[7]:
                    prob = 0
                else:
                    prob = 1
            
            # frame = cv2.resize(frame, (64, 64))
            
            if not success:
                break
            else:
                #face recog start
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(int(minW), int(minH)),
                )
                # my modifications
                if faces != []:
                    if(time.time()>=timer):
                        timer=timer+50
                        print("grand called in face detection",timer)
                        cv2.imwrite("suspect.png",frame)
                        result = idk("Medium level security is raised in Dwarakanagar. Get Moving! ","https://goo.gl/maps/ZcTaE9kFN5GL1CU67",["7483064938","7019486115","9380900636 "],["hemabhushanr3@gmail.com","sathvik.malgikar@gmail.com","rashmipr9496@gmail.com"])
                        
                idTemp = []
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
                    if id not in idTemp:
                        idTemp.append(id)
                    else:
                        pass

                    # If confidence is less them 100 ==> "0" : perfect match
                    if (confidence < 100):
                        id = names[id]
                        confidence = "  {0}%".format(round(100 - confidence))
                    else:
                        id = "unknown"
                        confidence = "  {0}%".format(round(100 - confidence))

                    cv2.putText(
                        frame,
                        str(id),
                        (x+5, y-5),
                        font,
                        1,
                        (255, 255, 255),
                        2
                    )
                    cv2.putText(
                        frame,
                        str(confidence),
                        (x+5, y+h-5),
                        font,
                        1,
                        (255, 255, 0),
                        1
                    )
               
                
                # if prob:
                #     print("prob")
                #     cv2.putText(frame, "Crime Detected", (200, 40), font, 1, (0, 0, 255), 1)
                
                # if(time.time()>=timer):
                #     print("grand called")
                #     cv2.imwrite("suspect.png",frame)
                #     whole.GRAND("Medium level security is raised in Dwarakanagar. Get Moving! ","https://goo.gl/maps/ZcTaE9kFN5GL1CU67",["7483064938","7019486115","9380900636 "],["hemabhushanr3@gmail.com","sathvik.malgikar@gmail.com","rashmipr9496@gmail.com"])
                #     timer=timer+50

                ret, buffer = cv2.imencode('.jpg', frame)
                
                
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
    return gen_frames

def init():
    for vid in vidStreams:
        vidFeeds.append(genVidFeed(vid))

init()


def auth(data):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    auth_db = client["Jaagrutha"]
    user_pass = auth_db["Auth"]
    queryResult = user_pass.find(data)
    for x in queryResult:
        return "1"
    return "0"

@app.route('/auth', methods=["GET", "POST"])
def home():
    return auth(json.loads(request.data))


@app.route('/feed', methods=["POST", "GET"])
def videofeed():
    id = int(request.args.get("id"))
    return Response(vidFeeds[id](), mimetype='multipart/x-mixed-replace; boundary=frame')
    
    

if __name__ == '__main__':
    app.run()