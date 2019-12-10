class Bank:
    def __init__(self,customers:[],numberOfCustomers:int,bankName:str):
        self.__customers = customers
        self.__numberOfCustomers = numberOfCustomers
        self.__bankName = bankName

    def Bank(self):
        return self.__bankName
    def addCustomer(self,firstName,lastname):
        self.__customers.append(firstName + " " + lastname)
        return self.__customers
    def getNumOfCustomers(self):
        return self.__numberOfCustomers
    def getCustomer(self,index):
        return self.__customers[index]



class Customer:
    def __init__(self,firstName:str,lastname:str):
        self.__firstName = firstName
        self.__lastname = lastname
        self.__account = Account(0)
    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastname
    def getAccount(self):
        return self.__account
    def setAccount(self,account):
        self.__account = account

class Account:
    def __init__(self,balance:float):
        self.__balance = balance
    def getBalance(self):
        return self.__balance
    def deposit(self,ammount):
        self.__balance += ammount
    def withdraw(self,ammount):
        if self.__balance < ammount:
            return False
        else:
            self.__balance -= ammount
            return True
            
Account1 = Account(100.0)
Customer1 = Customer('anjay','asyik')
Bank1 = Bank([],3,'ashiap')
print(Bank1.getNumOfCustomers())
print(Bank1.addCustomer('wkwkw','hehe'))



