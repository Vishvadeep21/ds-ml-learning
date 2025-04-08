def area(a,b,shape):
    total=0
    if shape=="rectangle":
        total=a*b
        print(total)
    elif shape=="triangle":
        total=(1/2)*a*b
        print(total)
    else:
        print("invalid values")
    return 0

x=area(2,2,"rectangle")
y=area(2,2,"triangle")