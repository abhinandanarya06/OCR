import time

def sort_chars(line):
  res = list()
  while len(line) > 0:
    mx = 100000
    m = 0
    for c in line:
      if c[1][0] <= mx:
        mx = c[1][0]
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
      if line[0][1][1] < mn:
        mn = line[0][1][1]
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
          if my <= c[1][1]+c[2][1]/2 and c[1][1]+c[2][1]/2 <= my_plus_h:
              if my > c[1][1]:
                my = c[1][1]
              if my_plus_h < c[1][1]+c[2][1]:
                my_plus_h = c[1][1]+c[2][1]
              lines[linei].append(c)
              characters.remove(c)
      lines[linei]= sort_chars(lines[linei])
      linei += 1
      characters.remove(m)
  return lines

