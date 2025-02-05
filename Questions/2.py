import statistics

d={"info":[600,630,620],
"ril":[1430, 1490, 1567],
"mtl":[234, 180, 160]}

while True:
    ip=int(input('''1.print
2.add
3.Exit
Enter yout choice: '''))
    
    def prt(d):
        for key,value in d.items():
            avg=statistics.mean(value)
            print(f"{key} -->{value} -->{avg}")
        return 0
  
    def add(d):
        a=input("Enter the stock ticker name: ")
        b=[]
        l=int(input("enter the number of stock you want to add"))
        for i in range(1,l+1):
            stock=int(input("enter stock: "))
            b.append(stock)
        if a in d:
            d[a].extend(b)
            print("key already exists and new value is added to it")
        else:
            d[a]=b
            print("New stock ticker and stock added successfully!!!")
        print(d)
        return 0
    if ip==1:
        prt(d)
    elif ip==2:
        add(d)
    elif ip==3:
        break
    else:
        print("put valid number between 1-3")
