'''
This module implements an Inventory class for a comic bookstore
Author: Marc Batete
'''
from inventoryLab import Inventory

class comicStoreInventory (Inventory):
    def __init__(self, name, price, quantity, \
                  cashier, time):

        self.cashier = cashier
        self.time = time

        Inventory.__init__(self, name, price, quantity )
    def getCashier(self):
        return self.cashier
    def getTimeStamp(self):
        return self.time
    def updateCashier(self, new):
        self.cashier = new
    def updateTimeStamp(self, new):
        self.time = new
    def __str__(self):
        item = self.name + "\t" + self.price + "$" +"\t" + self.quantity + "\t" + self.cashier + "\t" + self.time
        return item
