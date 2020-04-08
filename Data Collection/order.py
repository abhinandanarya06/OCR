from __future__ import print_function
import os

path = '/home/abhinandan/Downloads/gen/letters/'

files = os.listdir(path)
i = 7000
for name in files:
    if str(i)+'.jpg' != name:
        os.system('mv /home/abhinandan/Downloads/gen/letters/'+name+' /home/abhinandan/data/letters/'+str(i)+'.jpg')
        i+=1
