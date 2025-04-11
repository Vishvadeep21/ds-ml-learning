import numpy as np
a=np.arange(12).reshape(3,4)
print(a)

for x in np.nditer(a,order='c'):
    print(x)
for x in np.nditer(a,order='f'):
    print(x)

for x in np.nditer(a,order='f',flags=['external_loop']):
    y=x
    print(y)

for y in np.nditer(a,op_flags=['readwrite']):
    y[...]=y*y
    print(y)
    