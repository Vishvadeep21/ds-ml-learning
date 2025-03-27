#wap to calculate the questiont in a division operation
try:
    num=int(input("enter numerator"))
    den=int(input("Enter the denomenator"))
    quo=num//den
    print(quo)
except ValueError:
    print("please check your input")
except ZeroDivisionError:
    print("check the numbers entered")