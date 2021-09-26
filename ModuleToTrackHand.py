import cv2
import mediapipe as mp
import time
import math
import numpy as np


class handDetectorClass():
    def __init__(self, mode=False, maxHandsToBeDetected=2, detectionConfidence=0.5, trackConfidence=0.5):
        self.modeType = mode
        self.maxHandsToBeDetected = maxHandsToBeDetected
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.modeType, self.maxHandsToBeDetected,
                                        self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIdsOfFingers = [4, 8, 12, 16, 20]

    def findHandsInImageReturnImage(self, image, draw=True):
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLandmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLandmarks,
                                               self.mpHands.HAND_CONNECTIONS)

        return image

    def findPositionInImageReturnLandmarks(self, image, handNo=0, draw=True):
        xCoordList = []
        yCoordList = []
        boundingBox = []
        self.landmarkList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, landmark in enumerate(myHand.landmark):
                # print(id, landmark)
                h, w, c = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                xCoordList.append(cx)
                yCoordList.append(cy)
                # print(id, cx, cy)
                self.landmarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(image, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xCoordMin, xCoordMax = min(xCoordList), max(xCoordList)
            yCoordMin, yCoordMax = min(yCoordList), max(yCoordList)
            boundingBox = xCoordMin, yCoordMin, xCoordMax, yCoordMax

            if draw:
                cv2.rectangle(image, (xCoordMin - 20, yCoordMin - 20), (xCoordMax + 20, yCoordMax + 20),
                              (0, 255, 0), 2)

        return self.landmarkList, boundingBox

    def checkIfFingersUp(self):
        fingersBinaryValues = []
        # Thumb
        if self.landmarkList[self.tipIdsOfFingers[0]][1] > self.landmarkList[self.tipIdsOfFingers[0] - 1][1]:
            fingersBinaryValues.append(1)
        else:
            fingersBinaryValues.append(0)

        # Fingers
        for id in range(1, 5):

            if self.landmarkList[self.tipIdsOfFingers[id]][2] < self.landmarkList[self.tipIdsOfFingers[id] - 2][2]:
                fingersBinaryValues.append(1)
            else:
                fingersBinaryValues.append(0)

        # totalFingers = fingersBinaryValues.count(1)

        return fingersBinaryValues

    def findDistanceBetweenFingers(self, p1, p2, image, draw=True,r=15, t=3):
        x1, y1 = self.landmarkList[p1][1:]
        x2, y2 = self.landmarkList[p2][1:]
        centerx, centery = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(image, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(image, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(image, (centerx, centery), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, image, [x1, y1, x2, y2, centerx, centery]


def main():
    prevTime = 0
    currentTime = 0
    vidCap = cv2.VideoCapture(1)
    detector = handDetectorClass()
    while True:
        success, image = vidCap.read()
        image = detector.findHandsInImageReturnImage(image)
        landmarkList, boundingBox = detector.findPositionInImageReturnLandmarks(image)
        if len(landmarkList) != 0:
            print(landmarkList[4])

        currentTime = time.time()
        fps = 1 / (currentTime - prevTime)
        prevTime = currentTime

        cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)

        cv2.imshow("Image", image)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()