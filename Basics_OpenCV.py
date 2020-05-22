import cv2
 
img = cv2.imread("F:\\Projects\\OpenCV\\about3.jpg",1 )  #this is how to import the image 

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)) )#to resize the image  (divide the image to reduce size and multiply the image to increase the size)

cv2.imshow("Hero",resized) #This is how imshow function is used to show the image

cv2.waitKey(0) # 2000millisecond image will show then it will be disappeared automatically
cv2.destroyAllWindows()
