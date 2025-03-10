import numpy as np

a=np.arange(15).reshape(3,5)
print(a)

for i in a:
    print(i)

# flat

for cell in a.flat:
    print(cell)          #for getting each value from array
    