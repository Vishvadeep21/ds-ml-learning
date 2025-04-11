import numpy as np 
a=np.arange(12).reshape(3,4)
b=np.arange(3).reshape(3,1)

print(a)
print(b)

for x,y in np.nditer([a,b]):
    print(x,y)