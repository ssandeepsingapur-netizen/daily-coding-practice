class members:
    def __init__ (self,name,salary,pension):
        self.name = name
        self.salary = salary
        self.pension = pension

    def display(self):
        if self.salary<=50000:
            print("no pension get")
        else:
            print(self.salary + self.pension)
            
        

m1 = members("sandy" ,60000,400)
m1.display()
