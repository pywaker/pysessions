# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 18:33:55 2016

@author: sukrit
"""

from random import randint

class Client():
    def __init__(self,name,amount,number_passport):
        self._name = name
        self._amount = amount
        #self._type_account = type_account
        self._number_passport = number_passport
        n = [randint(0,9) for i in range(3)]
        self._account_num = self._name[:3].join(str(each) for each in n)
        
    def set_name(self,n_name):
        self._name = n_name
    
    def set_type_acc(self,n_type):
        self._type_account = n_type
        
    def set_amount(self,n_amount):
        self._amount = n_amount
        
    def take_money(self,amount):
        if amount > self._amount:
            return "Not enough money !!"
        else:
            self._amount = self._amount - amount
            return "Success !!",str(self._amount)
        
    def put_money(self,amount):
        self._amount += amount
        return "success!!","amount: "+str(self._amount)
    
    def bonus(self,percent):
        self._amount += (float(percent)/100)*self._amount
                
class Bank():
    def __init__(self,name):
        self._name = name
        self.clients = []
        
    def new_client(self,client):
        self.clients.append(client)
        
    def give_monthly_bonus(self,n):
        for client in self.clients:
            client.put_money(n)
            
    def give_bonus(self,p):
        for client in self.clients:
            client.bonus(p)
            
    def bonus_students(self,percent):
        for client in self.clients:
            if isinstance(client,Student):
                bonus = float(percent)/100*client._amount
                client.put_money(bonus)
                
    def search_client(self,num_passport):
        for client in self.clients:
            if num_passport == client._number_passport:
                return client
                
    def put(self,num_passport,a):
        c = self.search_client(num_passport)
        print(c.put_money(a))
        
    def take(self,num_passport,a):
        c = self.search_client(num_passport)
        print(c.take_money(a))
        
class Student(Client):
    def __init__(self,name,amount,number_passport): 
        Client.__init__(self,name,amount,number_passport)
        self.bonus_ = 20
        self._type_account = "student"
    def bonus(self,percent):
        self._amount += (float(percent+self.bonus_)/100)*self._amount
        
class Saving(Client):
    def __init__(self,name,amount,number_passport): 
        Client.__init__(self,name,amount,number_passport)
        self.bonus_ = 10
        self._type_account = "saving"
    def bonus(self,percent):
        self._amount += (float(percent+self.bonus_)/100)*self._amount
        
SB = Bank('SverBank')
SB.new_client(Student('Anton',100,1234))
SB.new_client(Student('Anna',randint(5000,100000),1563))
SB.new_client(Saving('Diana',randint(100000,500000),9685))
SB.new_client(Saving('John',randint(100000,500000),7584))

for each in SB.clients:
    print(each._name,str(each._amount),each._type_account,each._account_num)
    
SB.bonus_students(10)
print("-------------------------------")
        
for each in SB.clients:
    print(each._name,str(each._amount),each._type_account,each._account_num)

print("-------------------------------")

SB.give_bonus(10)

for each in SB.clients:
    print(each._name,str(each._amount),each._type_account,each._account_num)

print("-------------------------------")

p=9685
SB.put(p,2000)
p2=7584
SB.take(p2,5000)
        
        
        
        
        
        
        
        
        