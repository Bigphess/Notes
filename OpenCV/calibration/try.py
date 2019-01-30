import numpy as np 
import time

a = np.zeros((6*7,3),np.float32)
# a[:,:2] 
a =np.mgrid[0:2,0:3]
b = np.mgrid[0:2,0:3].T.reshape(-1,3)

print(time.asctime( time.localtime(time.time()) ))

arr = [['a','b'],[]]
str1 = ','.join(arr)

print(str1)