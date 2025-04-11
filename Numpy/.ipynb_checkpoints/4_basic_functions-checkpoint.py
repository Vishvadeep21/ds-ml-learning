import numpy as np

# zeros()
a=np.zeros((2,4))
print(a)

# ones()
b=np.ones((5,5))
print(b)

# araage()
c=np.arange(1,20,3)
print(c)

# linspace()
d=np.linspace(1,10,20)
print(d)

# reshape()
e=np.array([[1,2],[3,4],[5,6],[7,8]])
print(e.reshape(8,1))

# ravel()
print(e.ravel())

# dot()
x=e=np.array([[1,2],[3,4]])
y=e=np.array([[1,2],[3,4]])

print(x.dot(y))
# gives the matrix product