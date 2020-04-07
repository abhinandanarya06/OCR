from __future__ import print_function
import os

path = 'Downloads/gen/letters/'

files = os.listdir(path)
i = 6220
for name in files:
    if str(i)+'.jpg' != name:
        os.system('mv Downloads/gen/letters/'+name+' data/letters/'+str(i)+'.jpg')
        i+=1
