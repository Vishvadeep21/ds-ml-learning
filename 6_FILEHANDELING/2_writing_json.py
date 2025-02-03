import json

d={'NAME':'Vishvadeep','AGE':19,'NO':929392944}

file_path="Vishvadeep.json"

with open(file_path,"w") as file:
    json.dump(d,file,indent=5)
    # json.dump(dictionary,file,indentation)
    # json.dump is used  in place of file.write

    print(f"json file {file_path} is created successfully!!!")