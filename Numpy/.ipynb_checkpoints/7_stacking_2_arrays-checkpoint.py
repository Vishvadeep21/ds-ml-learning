import numpy as np

a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
c=np.vstack((a,b))
d=np.hstack((a,b))
print(c)
print(d)