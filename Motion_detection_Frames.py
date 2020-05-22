import cv2, time

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

check , frame = camera.read()

time.sleep(4)

cv2.imshow("Video", frame)

cv2.waitKey(0)

camera.release()

cv2.destroyAllWindows()