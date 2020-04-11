import cv2

character_list = [['a', (0,0), (1,1)], ['c', (0.1,1), (1,1)]]
line_list = list()
linei = 0
while len(character_list) > 0:
    m = character_list[0]
    line_list.append([m])
    for c in character_list[1:]:
        if m[1][0]+m[2][0] > c[1][0] and c[1][0] > m[1][0]-m[2][0]:
            line_list[linei].append(c)
            character_list.remove(c)
    linei += 1
    character_list.remove(m)

print(line_list)
print(character_list)
