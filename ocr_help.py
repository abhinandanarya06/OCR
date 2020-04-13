import cv2
import tensorflow as tf
import numpy as np


keywords = [chr(c) for c in range(ord('a'), ord('z')+1)]
cap = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'Q', 'R', 'T']
keywords = keywords + cap
keywords = keywords + ['noise']

X = 0
Y = 1
POS = 1
SHAPE = 2
W = 0
H = 1

def check_in(c, region):
    x, y, w, h = region
    center_x = c[POS][X]+c[SHAPE][W]/2
    center_y = c[POS][Y]
    if (center_x > x-1 and center_x < x+w+1) and (center_y > y-1 and center_y < y+h+1):
        return True
    return False

def get_region(c, regions):
    for region in regions:
        if check_in(char, region):
          return region
    return False

def sort_chars(line):
  res = list()
  while len(line) > 0:
    mx = 100000
    m = 0
    for c in line:
      if c[POS][X] <= mx:
        mx = c[POS][X]
        m = c
    line.remove(m)
    res.append(m)
  return res

def sort_lines_by_yval(lines):
  res = list()
  while len(lines) > 0:
    mn = 100000
    m = 0
    for line in lines:
      if line[0][POS][Y] < mn:
        mn = line[0][POS][Y]
        m = line
    lines.remove(m)
    res.append(m)
  return res

def group_chars_by_line(characters):
  lines = list()
  linei = 0
  while len(characters) > 0:
      m = characters[0]
      my = m[1][1]
      my_plus_h = m[1][1]+m[2][1]
      lines.append([m])
      for c in characters[1:]:
          if my <= c[POS][Y]+c[SHAPE][H]/2 and c[POS][Y]+c[SHAPE][H]/2 <= my_plus_h:
              if my > c[POS][Y]:
                my = c[POS][Y]
              if my_plus_h < c[POS][Y]+c[SHAPE][H]:
                my_plus_h = c[POS][Y]+c[SHAPE][H]
              lines[linei].append(c)
              characters.remove(c)
      lines[linei]= sort_chars(lines[linei])
      linei += 1
      characters.remove(m)
  return lines

def apply_ocr(img, text_detector):
    avg_h = 0
    character_list = list()
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
      except:
        continue
      test_data=np.array([test_data])
      cmd = np.argmax(text_detector.predict(test_data))
      if cmd < 40:
          avg_h += h
          cv2.rectangle(img, (x,y), (x+w+w//4, y+h), 255, -1)
          character_list.append([keywords[cmd], (x,y), (w,h)])
          i+= 1
    avg_h/=i
    text = group_chars_by_line(character_list)#, img)
    text = sort_lines_by_yval(text)
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    regions = list()
    for cnt in contours:
      region = cv2.boundingRect(cnt)
      if region[3] <= avg_h*7:
        regions.append(region)
    del contours

    TEXT = ''
    for l in text:
      char = l[0]
      region = get_region(char, regions)
      if not region:
        continue
      for char in l:
        if not check_in(char, region):
          TEXT = TEXT + ' '
          r = get_region(char, regions)
          if not r:
            continue
          region = r
        TEXT = TEXT + char[0]
      TEXT = TEXT + '\n'
    return TEXT
