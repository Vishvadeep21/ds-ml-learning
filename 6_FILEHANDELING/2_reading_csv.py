import csv

path="vd.csv"

with open(path,"r") as file:
    content=csv.reader(file)
    # thiswill give memory address only
    for i in content:
        print(i)
    print(f"the content in {path} file is: \n {i}")