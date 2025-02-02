# User defined functions
# lets understand it with an example
def summation(expense):
    total=0
    for i in expense:
        total+=i
    return total

a=[101,22,21,23]
totalsum=summation(a)
print(totalsum)