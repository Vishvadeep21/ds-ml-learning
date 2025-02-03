import csv
l=[["name","age","occ"],
   ["Vishvadeep",19,"data scientist"],
   ["Rajdeep",21,"scientist"]]

path="vd.csv"

with open(path,"w") as file:
    writer=csv.writer(file)
    # it creates the csv writer object
    for i in l:
        writer.writerow(i)
        # writerow() is used to add single line in csv files
        # to seprate each row
    print("FILE WAS CREATED SUCCESSFULLY")