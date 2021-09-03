import cv2
from cvzone.HandTrackingModule import HandDetector

capture = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)
handTypes = []
fingers = []

while True:
    success, image = capture.read()
    hands,image = detector.findHands(image) # find Hands from image
    landMarks = []

    cv2.imshow("Image",image)


    # Get
    if hands:
        for hand in hands:
            # print("Total Hand Details", hand)
            # print("\n\n==================================================")
            landMark = hand["lmList"] # List of the all 21 Landmarks points for hand
            landMarks.append(landMark)
            boundingBox = hand["bbox"] # Bounding Box info such as x,y,w,h
            centralPoint = hand["center"] # center of the hand cx.cy
            handType = hand["type"] # Hand type left or right
            # print("LandMark List: ",landMark)
            # print("Bounding Box: ", boundingBox)
            # print("Central Point: ", centralPoint)
            print("HandType: ", handType) # show the left or right
            handTypes.append(handType)
            finger = detector.fingersUp(hand)
            # print(finger)

            for lmark in landMark:
                print("Lmark: ",lmark)

           # Get the distance between two finger(landmark point)
           # length, info, image = detector.findDistance(landMark[8], landMark[12], image)

            showAllHandTypes = ' '.join([str(elem) for elem in handTypes])
            # print("ShowAllHands: ", showAllHandTypes)

    # if landMarks:
    #     print(landMarks)
    #     if landMarks[0]:
    #         if len(landMarks)>1:
    #             length , info , image = detector.findDistance(landMarks[0][8],landMarks[1][8],image)
    #         else:
    #             length, info, image = detector.findDistance(landMarks[0][8], landMarks[0][12], image)

    # if cv2.waitKey(0) & 0xFF:
    #     break

    cv2.waitKey(1)
