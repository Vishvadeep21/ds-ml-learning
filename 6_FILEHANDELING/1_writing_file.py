employee=["apple","banana","kela"]

file_id="Employeeid.txt"

with open(file_id,"a") as file:
    for i in employee:
        file.write(i+"\n")
    print("added successfully")
