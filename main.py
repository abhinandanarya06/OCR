import cv2
from ocr_help import *

imgs = [f for f in os.listdir('.') if f.endswith('.jpg')]
img_no = 0
for img in imgs:
    avg_w = 0
    avg_h = 0
    character_list = list()
    img = cv2.imread(img)
    color = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,5)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,21,10)
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img[:,:]=0
    i = 0
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
          avg_w += w
          avg_h += h
          cv2.rectangle(img, (x,y), (x+w+w//3, y+h), 255, -1)
          character_list.append([keywords[cmd], (x,y), (w,h)])
          i+= 1
        #cv2.imwrite('gen/'+keywords[cmd]+'/'+str(i)+'.jpg', show)
        #i+=1
      except:
            continue
    avg_w/=i
    avg_h/=i
    text = group_chars_by_line(character_list)#, img)
    text = sort_lines_by_yval(text)
    print('*'*30, 'Text in image', imgs[img_no], '*'*30,'\n')
    imshow(color)

    img = cv2.blur(img,(8,1))
    ret, img = cv2.threshold(img,254,255,cv2.THRESH_BINARY)
    kernel = np.ones((3,10),np.uint8)
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    regions = list()
    for cnt in contours:
      region = cv2.boundingRect(cnt)
      if region[3] <= avg_h*7:
        regions.append(region)
    del contours
    for l in text:
      char = l[0]
      region = get_region(char, regions)
      if not region:
        continue
      for char in l:
        if not check_in(char, region):
          print(end=' ')
          r = get_region(char, regions)
          if not r:
            continue
          region = r
        print(char[0], end='')
      print()
    print('-'*80, '\n\n')
    img_no += 1
