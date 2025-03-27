# steps: 1.Create a var for text file data 
        #  2.give path in var
        #  3.open file and using write function add text data to it


txt_data="Hello this is vishvadeep"
# Text data is always in string 
file_name="hello.txt"
# we can create new files or can give path from other directories
try:
    with open(file_name, "w") as file:
    # w= write
    # a= append
    # x= creates new file(gives error if already exist)
        file.write(txt_data)
        print(f"succesfully added to {file_name}") 
except FileExistsError:
    print("file exists")