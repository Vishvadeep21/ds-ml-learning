#  Class:- A template for creating objects. Defines properties and behaviors
# Objects:- A specific instance of a class with actual values.
# used in the concept of oops 
class Human():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def namee(self):
        print(f"hello {self.name} how are you!!!")

    def agee(self):
        print(f"You are {self.age} years old!!!")

vd=Human("Vishvadeep",18)
rd=Human("Rajdeep",20)
vd.namee()
vd.agee()
rd.namee()
rd.agee()

# here rd and vd are objects of class