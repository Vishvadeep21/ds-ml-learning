import csv

l=[["company name","price","earnings per share","book value"],
   ["reliance",1467,66,635],
   ["tata steel",391,89,572]
   ]

path="stocks.csv"

with open(path,"w") as file:
    write=csv.writer(file)
    write.writerows(l)
    print("added successfully!!!")