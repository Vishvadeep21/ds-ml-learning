contracts={'vishvadeep':9389534860,'Sayyed Hussain':1365468210,'Dev':3288789512,'Prajwal':2122154800}
while True:
    user=int(input('''enter your choice
1.print
2.add
3.remove
4.query:- '''))
    if user==1:
        for key,value in contracts.items():
            print(f"{key}=>{value}")
    
    elif user==2:
        k=input("enter the name for new contract: ")
        v=int(input("enter the phone number for new contract: "))
        if k in contracts:
            print("contract already exists!!!")
        else:
            contracts[k]=v
            print("contracts updated succesfully!!!")
            print(contracts)
    elif user==3:
        r=input("enter the contract you want to remove: ")
        if r not in contracts:
            print("contract doesn't exist!!!")
        else:
            del contracts[r]
            print("Contract removed successfully!!!")
        print(contracts)
    elif user==4:
        q=input("Enter the contract in which you want query")
        if q not in contracts:
            print("contract doesn't exist!!!")
        else:
            print(f"{q}=>{contracts[q]}") 
    else:
        break