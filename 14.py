class Bank:
    def __init__(self,bank_name,holder_name,id,age):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.id = id
        self.age = age

    def create_account(self):
        if self.age>=18:
            print("Bank name:",self.bank_name)
            print("Person name :",self.holder_name)
            print("Bank ID :", self.id)
            print("account created succesful")

        else:
            print("age is  was not matched")


bank_name = input("enter name of bank")
holder_name =  input("enter name of person")
id = input("enter your id")
age = int(input("enter the age "))


B = Bank(bank_name,holder_name,id,age)
B.create_account()