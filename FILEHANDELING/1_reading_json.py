import json

path="vishvadeep.json"
try:    
    with open(path,"r") as file:
        content=json.load(file)
        print(f"the content of {path} file is : \n {content}")
except FileNotFoundError:
    print(f"The file named '{path} did not fount in your pc!!!")