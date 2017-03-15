# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:12:47 2017

@author: Mohit
"""

class SMS_store():
    count=0
    def __init__(self,name):
        self._name = name
        self.message = []
        
    
    def add_new_arrival(self,message):
        self.message.append(message)
        SMS_store.count += 1
    
    def message_count(self):
        return SMS_store.count
             
    def read_message(self,i):
        print(Message.get_from_number(self.message[i]))
        print(Message.get_time_arrived(self.message[i]))
        print(Message.get_text(self.message[i]))
        self.message[i].has_been_viewed=True
                    
    def get_unread_indexes(self):
        #list1 = []
        for each in range(len(self.message)):
            if self.message[each].has_been_viewed != True:
                print(each)
                
    def delete(self,i):
        if not self.message:
            print("List is empty")
        else:
            del self.message[i]
            SMS_store.count -= 1
            
    def clear(self):
        del self.message[:]
        SMS_store.count = 0
     
class Message(): 
    def __init__(self,number,time,text):
        self.from_number = number
        self.time_arrived = time
        self.text_of_sms = text
        self.has_been_viewed = False
        
    def get_from_number(self):
        return self.from_number
    
    def get_time_arrived(self):
        return self.time_arrived
    
    def get_text(self):
        return self.text_of_sms
    
   
    
    
    
inbox = SMS_store("Mobile")
inbox.delete(2)
print("-------------------------------")
inbox.add_new_arrival(Message("9841016667","7 AM","Hey, There!!!"))   
inbox.add_new_arrival(Message("9841261019","8 AM","Hey,How are you!!!")) 
inbox.add_new_arrival(Message("9860222222","9 AM","Hello, can you here me")) 
inbox.add_new_arrival(Message("9843857027","10 AM","I was wondering if all these years")) 

for each in inbox.message:
    print(str(each.from_number),each.time_arrived,each.text_of_sms,each.has_been_viewed)  
print("-------------------------------")
print(inbox.message_count())
print("-------------------------------")
#print(inbox.message[1].from_number)
#print(Message.get_from_number(inbox.message[1]))
inbox.read_message(2)
inbox.read_message(1)
print("-------------------------------")
inbox.get_unread_indexes()
print("-------------------------------")
inbox.clear()
print(inbox.message_count())

