import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time

path = "testimages"
images = []
className = []

myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    className.append(os.path.splitext(cl)[0])
# print(className)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


def markAttendance(rollno):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        rollNoList = []
        for line in myDataList:
            entry = line.split(",")
            rollNoList.append(entry[0])
        if rollno not in rollNoList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f'\n{rollno},{dtString}')


encodeListKnown = findEncodings(images)
print(len(encodeListKnown))

print("--VIDEO CAMERA ABOUT TO START--")
cap = cv2.VideoCapture(0)
print("-----VIDEO CAMERA STARTED------")

totalFrames, countFrame = 0, 0

starttime = time.time()

while True:
    success, img = cap.read()

    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    if time.time() - starttime > 10:
        totalFrames = totalFrames + 1
        faceFrame = face_recognition.face_locations(imgSmall)
        encodeFrame = face_recognition.face_encodings(imgSmall, faceFrame)

        for encodeFace, faceLoc in zip(encodeFrame, faceFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex]:
                countFrame = countFrame + 1
                rollNo = className[matchIndex].upper()
                markAttendance(rollNo)
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
