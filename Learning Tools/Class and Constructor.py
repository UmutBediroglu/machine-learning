# -*- coding: utf-8 -*-

class worker:
    
    raise_rate1 = 1.8
    counter = 0
    
    def __init__(self, name, surname, payment): #constructor
        self.name = name
        self.surname = surname
        self.payment = payment
        self.email = name + surname + "@gmail.com"
        worker.counter+=1 #How many worker they have
        
    def giveNameSurname (self):
        return self.name + " " + self.surname
    
    def raise_rate(self):
        self.payment = self.payment + self.payment * self.raise_rate1
    
worker1 = worker("Mehmet", "Ozan", 100)
worker2 = worker("Ali", "Ozan", 150)
worker3 = worker("Eren", "Ozan", 500)
worker4 = worker("Okan", "Ozan", 250)

print("Worker1 Payment:", worker1.payment)

worker1.raise_rate()
print("Worker1 New Payment:", int(worker1.payment))

print(worker.counter)

#%%

max_payment = -1
index = -1

list1 = [worker1, worker2, worker3, worker4]

for i in list1:
    if (i.payment > max_payment):
        max_payment = i.payment
        index = i
        
print(max_payment)
print(index.giveNameSurname())

