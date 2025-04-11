import numpy as np

a=np.arange(30).reshape(3,10)
print(np.hsplit(a,2))
print(np.vsplit(a,1))