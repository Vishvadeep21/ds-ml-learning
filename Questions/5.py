class employee():
    def __init__(self,id,role):
        self.id=int(id)
        self.role=role

    def display(self):
        print(f"id:{self.id}, role:{self.role}")

vd=employee(15031,"Data Scientist")
vd.display()
rd=employee(15011,"Data Analyst")
rd.display()