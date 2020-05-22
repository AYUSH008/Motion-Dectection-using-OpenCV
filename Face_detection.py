import cv2

#create Cascade object
face_cascade = cv2.CascadeClassifier('F:\\Projects\\OpenCV\\haarcascade_frontalface_default.xml')

#read the image from system
img = cv2.imread("F:\\Projects\\OpenCV\\ironman.jpg",1 )

#convert image to gray scale image
gray_img = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

#search the coordinates of  an image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5 )

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img= cv2.rectangle(img , (x,y), (x+w, y+h), (0,255,0),3)
    

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)) )

cv2.imshow("Gray",resized) #This is how imshow function is used to show the image

cv2.waitKey(0) # 2000millisecond image will show then it will be disappeared automatically
cv2.destroyAllWindows()