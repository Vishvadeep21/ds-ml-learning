contacts={'vishvadeep':9389534860,'Sayyed Hussain':1365468210,'Dev':3288789512,'Prajwal':2122154800}
while True:
    user=int(input('''enter your choice
1.print
2.add
3.remove
4.query
5.end:- '''))
    
    def prt():
        for key,value in contacts.items():
            print(f"{key}=>{value}")
    
    def add():
        k=input("enter the name for new contact: ")
        v=int(input("enter the phone number for new contact: "))
        if k in contacts:
            print("contact already exists!!!")
        else:
            contacts[k]=v
            print("contacts updated succesfully!!!")
            for key,value in contacts.items():
                print(f"{key}=>{value}")
    def  remove():
        r=input("enter the contact you want to remove: ")
        if r not in contacts:
            print("contact doesn't exist!!!")
        else:
            del contacts[r]
            print("Contract removed successfully!!!")
        for key,value in contacts.items():
            print(f"{key},{value}")
    def query():
        q=input("Enter the contract in which you want query: ")
        if q not in contacts:
            print("contact doesn't exist!!!")
        else:
            print(f"{q}=>{contacts[q]}") 

    match user:
        case 1:
            prt()
        case 2:
            add()
        case 3:
            remove()
        case 4:
            query()
        case 5:
            break
