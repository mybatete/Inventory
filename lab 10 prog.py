from lab10_classe import items

"""PROGRAM : 	Employee	Database
Author : batete Yedidia Marc
E-mail: mybatete@lcmail.lcsc.edu
Date: 04/15/2018
Description: the program creates an items electronic database by using dictionnary and classes data structures and making the given data easier to manipulate.
Inputs: Inventory_worksheet.dat

output :
1.	Display	the	price	of	item-40.
2.	Item-173	is on	sale	and	is	now	50%	off	the	price. Update	and	display	the	new	price.
3.	Purchasing	of	a	quantity	of	3	items	of	item-569.	Display	the	new	amount	in	stock.
4.	The	customer	returns	two	quantities	of item-237 back	to	the	store.	Display	the	new	amount	in	stock.
5.	Query	the	dictionary	to	report	all	items	that	have	low	stock	levels	(i.e.	quantity	in	stock	is	<	15)	
6.	Calculate	the	total dollar	amount of	the	retail	store’s	merchandise.	

"""
ft = open ("Inventory_worksheet.dat","r")
dic = {}
ft.readline()

while True:
    line = ft.readline()
    if line == "":
        break
    line = line.strip()
    word = line.split()
    name = word[0]
    price = float(word[1])
    qty = int(word[2])
#the program assigns the object as the value and uses the name of the item as key
    s = items(name, price, qty)
    dic[name] = s


a= dic.get("item-40")
print "the item-40 costs: ", a.getPrice(),"$"
b= dic.get("item-173")
b.getPrice()
print "the new price of item-173 is: ", (((b.getPrice())*50)/100.0),"$"
c= dic.get("item-569")
c.purchaseItem(3)
print "there are ",c.getQuantity(), "item-569 left"
d = dic.get("item-237")
d.returnItem(2)
print "there is now",d.getQuantity(), "item-237"
total_marchandise = 0
for item in dic:
    s = dic.get(item)
    b = s.getQuantity()
    p = s.getPrice()
    total_marchandise = total_marchandise + p
    if b < 15 :
        print item
print "the total dollar amount of the retail store's merchandise is: ", total_marchandise
ft.close()
