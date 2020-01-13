"""PROGRAM : 	Employee	Database
Author : batete Yedidia Marc
E-mail: mybatete@lcmail.lcsc.edu
Date: 04/20/2018
Description: the program creates an items electronic database by using dictionnary and classes data structures and making the given data easier to manipulate.
Inputs: Inventory.dat
        comicStoreInventory

output :
1. query the dictionary to display the information on item-176 and item-822
============== RESTART: C:/Users/student/Desktop/mine/lab11.py ==============
item-176	9.99$	198	Cashier-4	14:43
item-822	36.99$	121	Cashier-5	12:29
"""
from deux import comicStoreInventory

ft = open ("Inventory.dat","r")
#create a dictionarry empty
dic = {}
#read the first line of the text because its the headline and we dont want it.
ft.readline()
#loop through the text
while True:
    line = ft.readline()
    if line == "":
        break
    line = line.strip()
    word = line.split()
    name = word [0]
    price = word [1]
    quantity = word [2]
    cashier = word [3]
    time = word [4]
#get each of the values in the text and create an inventory for each of their values.
    
    s = comicStoreInventory (name, price, quantity, cashier, time)
    #save their value in the dictonnary using the name as key.
    dic[name] = s

#look up the items.
s = dic.get("item-176")
k = dic.get("item-822")
#print them out.
print str(s)
print str(k)

