country={'China':143,'India':136,'USA':32,'Pakistan':21}
while True:
    user=int(input('''enter your choice
1.print
2.add
3.remove
4.query:- '''))
    if user==1:
        for key,value in country.items():
            print(f"{key}=>{value}")
    
    elif user==2:
        k=input("enter the key for new dictionary: ")
        v=int(input("enter the value for new dictionary: "))
        if k in country:
            print("item already exists!!!")
        else:
            country[k]=v
            print("Dictionary updated succesfully!!!")
            print(country)
    elif user==3:
        r=input("enter the country you want to remove: ")
        if r not in country:
            print("item doesn't exist!!!")
        else:
            del country[r]
            print("Country removed from dictionary successfully!!!")
        print(country)
    elif user==4:
        q=input("Enter the country in which you want query")
        if q not in country:
            print("item doesn't exist!!!")
        else:
            print(f"{q}=>{country[q]}") 
    else:
        break