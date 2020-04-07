import cv2
import numpy as np
cv2.namedWindow('big', cv2.WINDOW_NORMAL)
cv2.namedWindow('mag', cv2.WINDOW_NORMAL)
images = ['1.jpg']
file=open('data/data.txt', 'w')
i = 0
for img in images:
    img = cv2.imread(img, 0)
    color = img
    img = cv2.medianBlur(img,5)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,41,10)
    #img = cv2.Canny(img,100,100)
    cv2.imwrite('a.jpg', img)
    img = cv2.multiply(img, 2)
    draw = img.copy()
    draw[:][:] = 0
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        try:
            x,y,w,h = cv2.boundingRect(c)
            big = color.copy()
            cv2.rectangle(big,(x, y),(x+w,y+h),(0,255,0),-1)
            try:
                show = color[y-2:y+h+2, x-2:x+w+2]
                big = big[y-10:y+h+10, x-80:x+w+80]
            except:
                show = color[y:y+h, x:x+w]
                big = big[y:y+h, x:x+w]

            cv2.imshow('big', big)
            cv2.imshow('mag', show)
            cmd = probablity(show)
            if cmd == ord(' '):
                file.write(str(i)+'.jpg 1\n')
            elif cmd == ord('q'):
                break
            else:
                file.write(str(i)+'.jpg 0\n')
            cv2.imwrite('data/'+str(i)+'.jpg', show)
            i+=1
        except:
            pass
print(i)
