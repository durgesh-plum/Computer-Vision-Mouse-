import cv2
import numpy as np
import ModuleToTrackHand as mtth
import time
import pyautogui
import time


popUpWindowName='Computer Vision - Mouse'

##########################
widthCam, heightCam = 640, 480
frameReduction = 150  # Frame Reduction
smootheningValue = 4
#########################

prevTime = 0
prevlocX, prevlocY = 0, 0
currentlocX, currentlocY = 0, 0

videoCap = cv2.VideoCapture(0)
videoCap.set(3, widthCam)
videoCap.set(4, heightCam)
handDetector = mtth.handDetectorClass(maxHandsToBeDetected=1)
# widthScr, heightScr = autopy.screen.size()
widthScr, heightScr = pyautogui.size()
# print(widthScr, heightScr)

success, image = videoCap.read()
time.sleep(1)
h,w,c=image.shape
cv2.namedWindow(popUpWindowName)

cancelBoxDimen=50
closeProgram=False
def mouseClicked(event, x, y, flags, param):
    global closeProgram
    if event == cv2.EVENT_LBUTTONDOWN:
        if (w-cancelBoxDimen)<x<w and 0<y<cancelBoxDimen:
            closeProgram=True
            # print("closeProgram1")

while videoCap.isOpened():
    # Find Landmarks
    # time.sleep(0.1)
    success, image = videoCap.read()
    image = cv2.flip(image, 1)

    #==============================GUI==============================
    image = cv2.rectangle(image, (w-cancelBoxDimen,0), (w,cancelBoxDimen), (0,0,255), -1)
    image = cv2.rectangle(image, (w-cancelBoxDimen,0), (w,cancelBoxDimen), (255,255,255), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    # org = (w-cancelBoxDimen+10, cancelBoxDimen-10)
    fontScale = 1
    color = (255, 255, 255)
    thickness = 5
    text='X'
    textsize = cv2.getTextSize(text, font, fontScale, thickness)[0]
    textX = int((w-(cancelBoxDimen/2)) - (textsize[0] / 2))
    textY = int((cancelBoxDimen/2) + (textsize[1] / 2))
    # cv2.putText(image, text, (textX, textY ), font, 1, (255, 255, 255), 2)
    image = cv2.putText(image, text, (textX, textY ), font, fontScale, color, thickness, cv2.LINE_AA)
    ##==============================#==============================

    image = handDetector.findHandsInImageReturnImage(image)
    landmarkList, bbox = handDetector.findPositionInImageReturnLandmarks(image)
    # Get tip of the index & middle fingers
    if len(landmarkList) != 0:
        x1, y1 = landmarkList[8][1:]
        x2, y2 = landmarkList[12][1:]
        # print(x1, y1, x2, y2)

     #which fingers are up check
    try:
        fingers = handDetector.checkIfFingersUp()
        cv2.rectangle(image, (frameReduction, frameReduction), (widthCam - frameReduction, heightCam - frameReduction),(255, 0, 255), 2)
        # Only Index Finger Up, therefore Moving Mode is ON
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0:
            # Convert Coordinates to match our resolution
            x3 = widthScr - np.interp(x1, (frameReduction, widthCam - frameReduction), (0, widthScr))
            y3 = np.interp(y1, (frameReduction, heightCam - frameReduction), (0, heightScr))
            # Smoothen Values to show intermediate cursors
            currentlocX = prevlocX + (x3 - prevlocX) / smootheningValue
            currentlocY = prevlocY + (y3 - prevlocY) / smootheningValue

            # Move Mouse only when index finger raised
            pyautogui.moveTo(widthScr - currentlocX, currentlocY)
            cv2.circle(image, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            prevlocX, prevlocY = currentlocX, currentlocY

        #Index and middle fingers are raised, left clicking Mode on
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:
            # Distance between Index and middle fingers
            length, image, lineInfo = handDetector.findDistanceBetweenFingers(8, 12, image)
            # Click mouse if, distance short
            if length < 40:
                cv2.circle(image, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                pyautogui.click(button='left')

        #Index and middle fingers are up : right clicking Mode ON
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
            #Find distance between fingers to right click
            length, image, lineInfo = handDetector.findDistanceBetweenFingers(8, 12, image)
            #Right Click mouse if distance short
            if length < 40:
                cv2.circle(image, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                pyautogui.click(button='right')

    except:
        # print("No finger")
        pass

    # 11. Frame Rate
    currentTime = time.time()
    fps = 1 / (currentTime - prevTime)
    prevTime = currentTime
    cv2.putText(image, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.setMouseCallback(popUpWindowName, mouseClicked)

    if closeProgram:
        #print("closeProgram2")
        break

    cv2.imshow(popUpWindowName, image)
    cv2.waitKey(1)


videoCap.release()
# Destroy all the windows
cv2.destroyAllWindows()