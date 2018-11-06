'''
in case you are intrested in downloaloading a more image for testing, so the below snippet can be used for sorting.
Rename the downloaded images in sequence.
'''
#/usr/bin/python

import os
import time

start = time.time()
path = '/home/user/Downloads/groupfaces'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1

print("TotalTime", time.time()-start)#TotalTime 0.011953353881835938