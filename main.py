import cv2
from ocr_help import *


imgs = [f for f in os.listdir('.') if f.endswith('.jpg')]
#i = 0
img_no = 0
for img in imgs:
    character_list = list()
    img = cv2.imread(img)
    color = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,5)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,21,10)
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
      try:
        x,y,w,h = cv2.boundingRect(c)
        try:
            show = color[y-2:y+h+2, x-2:x+w+2]
        except:
            show = color[y:y+h, x:x+w]
        test_data = cv2.resize(show,(50,50),interpolation = cv2.INTER_AREA)
        test_data=np.array([test_data])
        cmd = np.argmax(probablity.predict(test_data))
        if cmd < 40:
          character_list.append([keywords[cmd], (x,y), (w,h)])
        #cv2.imwrite('gen/'+keywords[cmd]+'/'+str(i)+'.jpg', show)
        #i+=1
      except:
            continue
    text = group_chars_by_line(character_list)#, img)
    text = sort_lines_by_yval(text)
    print('*'*30, 'Text in image', imgs[img_no], '*'*30,'\n')
    imshow(img)
    addw = dno = 0
    for l in text:
      wno = 1
      for w in l[:-1]:
          fut = l[wno]
          wid = fut[1][0]-w[1][0]
          addw += wid
          dno += 1
          avg_width = addw/dno
          print(w[0], end='')
          if wid >= avg_width*1.08:
            print(end=' ')
          wno += 1
      print()
    print('-'*80, '\n\n')
    img_no += 1
