import numpy as np
import cv2
img = cv2.imread('/Users/ashukumar/Downloads/m.jpg',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('messigray.png',img) #save images first argument nameof the saved file second argument the data to be saved
 
