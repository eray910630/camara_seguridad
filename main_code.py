
import numpy
import cv2
import time
import winsound

def different(newpict, frame, frame2):
    newframe = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    newframe2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)

    p1 = cv2.absdiff(newframe2, newpict)
    p2 = cv2.absdiff(newpict, newframe)
    p3 = cv2.absdiff(p1, p2)

    #cv2.imshow("diff", p3)
    diff3 = cv2.sumElems(p3)
    #print(diff3)
    return diff3[0]

def main():
    #calibrate = 700000
    cap = cv2.VideoCapture(0)
    time.sleep(2) #waiting for the webcam
    ret, pict = cap.read()
    picture = cv2.cvtColor(pict, cv2.COLOR_RGB2GRAY)
    calibrate = calibration(10, cap, picture)
    frec, d = 2500, 500
    while(ret):
        # Capture frame-by-frame
        ret, frame = cap.read()
        ret, frame2 = cap.read()
        diff = different(picture, frame, frame2)
        if(diff > calibrate):
            print("A thief!!!!!!!!!!!!")
            winsound.Beep(frec, d)

        # Display the resulting frame
        cv2.imshow("Security Camera Output", frame)
        if (cv2.waitKey(2) == 27):
            break

    cap.release()
    cv2.destroyAllWindows()


def calibration(n, cap, picture):
    time.sleep(2)
    #cap = cv2.VideoCapture(0)
    #ret, picture = cap.read()
    ret, f = cap.read()
    ret, f2 = cap.read()
    res = different(picture, f, f2)
    for i in range(2, n):
        ret, f = cap.read()
        ret, f2 = cap.read()
        temp = different(picture, f, f2)
        if(temp > res):
            res = temp
    #cap.release()
    print(res)
    return res

main()
