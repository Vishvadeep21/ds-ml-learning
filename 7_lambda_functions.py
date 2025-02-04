# Usefull to create the small functions in a single line
# Also for creating function inside the function
double=lambda x: x*x
# print(double(2))
cube=lambda x: x**3
# print(cube(3))

# the example if function inside the function
def fun(fx,value):
    return fx(value)+10
z=int(input("enter the number:"))
print(fun(lambda x:x * 2,z))