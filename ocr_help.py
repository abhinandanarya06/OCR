import cv2
import tensorflow as tf
import numpy as np

### FOR MAPPING BETWEEN MODEL RESULT NUMBERS AND ITS CORRESPONDING CHARACTERS
keywords = [chr(c) for c in range(ord('a'), ord('z')+1)]
cap = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'Q', 'R', 'T']
keywords = keywords + cap
keywords = keywords + ['noise']

# SOME CONVENTION FOR BELOW FUNCTION DEFINATION
X = 0   # X coordinate of the character in image space
Y = 1   # Y coordinate of the character in image space
POS = 1    # shows and return the (x,y) coordinate of image space
SHAPE = 2  # shows and return the (width, height) of character contour in image space
W = 0 # width of the character
H = 1 # height of the character


def check_in(c, region):
    '''
Purpose: Check if character "c" present in word region "region"
Input  : 1) character "c" with its position and shape-size
         2) "region" with its rectangular vertices coordinates
Output : return True if "c" is present in "region" else False
    '''
    x, y, w, h = region
    center_x = c[POS][X]+c[SHAPE][W]/2
    center_y = c[POS][Y]
    if (center_x > x-1 and center_x < x+w+1) and (center_y > y-1 and center_y < y+h+1):
        return True
    return False


def get_region(c, regions):
    '''
Purpose : Get one region from list of regions "regions" where character "c" is present
Input   : 1) character "c" with its position and shape-size
          2) list of regions "regions" each having its rectangular vertices coordinates
Output  : Return the region from list of regions where c is belonging
            if region not found, return False
Approach: Linear Search
    '''
    for region in regions:
        if check_in(c, region):
          return region
    return False

def sort_chars(line):
    '''
Purpose : Sorts characters in a line (list of characters)
Input   : "line" list of characters
Output  : "res" sorted list of characters
Approach: Selection Sort
    '''
    return sorted(line, key=lambda c: c[POS][X])


def sort_lines_by_yval(lines):
    '''
Purpose : Sort the line by its y coordinate value
Input   : "lines" list of lines
Output  : "res" sorted list of lines
Approach: Selection Sort
    '''
    return sorted(lines, key=lambda line: line[0][POS][Y])


def group_chars_by_line(characters):
    '''
Purpose : Group text characters by lines
Input   : "characters" list of characters with its position and height given in list itself
Output  : "lines" list of lines itself list of characters
Approach: Linear Search for each line
    '''
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

'''
    "apply_ocr(img)" is the function that does actual ocr
    operation on image parameter to get text
'''
def apply_ocr(img, text_detector):
    avg_text_height = 0 # will be assigned with Average Height of text character
    character_list = list() # will contain necessary text character to be extracted
    img = cv2.medianBlur(img,5)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,41,10) # will remove maximum noise and make image suitable for contour dt
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    black_map = img.copy()
    black_map[:, :] = 0
    i = 0
    for contour in contours:
        try:
            x,y,w,h = cv2.boundingRect(contour)
            try:
                cnt = img[y-2:y+h+2, x-2:x+w+2]
            except:
                cnt = img[y:y+h, x:x+w]
            cnt = cv2.resize(cnt, (30, 30), interpolation = cv2.INTER_AREA)
            cnt = cnt.reshape((1, 30, 30, 1))
            cnt = cnt / np.max(cnt.reshape(900))
            class_pred = np.argmax(text_detector.predict(cnt))
            if class_pred < 40:
                avg_text_height += h
                cv2.rectangle(black_map, (x-w//7,y), (x+w+w//7, y+h), 255, -1)
                character_list.append([keywords[class_pred], (x,y), (w,h)])
                i += 1
        except:
              continue
    avg_text_height /= i # Average Height of text character
    text = group_chars_by_line(character_list)
    text = sort_lines_by_yval(text)
    contours, hierarchy = cv2.findContours(black_map, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    regions = list() # will contain regions of words for grouping chars by word
    for contour in contours:
        region = cv2.boundingRect(contour)
        if region[SHAPE + H] <= avg_text_height*7:
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
