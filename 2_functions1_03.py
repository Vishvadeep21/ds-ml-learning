# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3
def pattern(a):
    for i in range(a):
        print((i+1)*"*")
    return 0
c=int(input("enter the number of lines to print: "))
b=pattern(c)