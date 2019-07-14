'''
ROI工具
手動圈選區域追蹤
'''

import cv2
tracker = cv2.TrackerCSRT_create()
cap = cv2.VideoCapture('human.avi')
initTarget = None
while True:
    ret, frame = cap.read()
    if initTarget is None:
        initTarget = cv2.selectROI('video', frame)
        tracker.init(frame, initTarget)
    else:
        success, rect = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(i) for i in rect]                    #單位是Pixel
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('video', frame)

    if cv2.waitKey(66) == 27:
        cv2.destroyAllWindows()
        break
