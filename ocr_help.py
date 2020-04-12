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
