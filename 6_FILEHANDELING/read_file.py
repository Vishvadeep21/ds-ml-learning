path="hello.txt"
try:    
    with open(path,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File was not found!!!")