import cv2

vid = cv2.VideoCapture(1)
from time import sleep


while(True):
    
    ret, frame = vid.read()
    
    sleep(1)
    
    cv2.imshow("Jaagratha.",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
vid.release()

cv2.destroyAllWindows()
exit()