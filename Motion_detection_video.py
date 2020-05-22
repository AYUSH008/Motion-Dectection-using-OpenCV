import cv2, time

camera = cv2.VideoCapture(0 ,)

a = 1

while True:
    a=a+1
    check, frame = camera.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("capturing video", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


print(a)
camera.release()
cv2.destroyAllWindows()