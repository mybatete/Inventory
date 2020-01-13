'''
This module implements a Retail Inventory Class
This is for creating item objects

'''

class Inventory (object):

	#Class Variable definition
	DISCOUNT= 0.05

	def __init__(self, name, price, quantity):
		""" Initializes the instance variables"""

		self.name     = name
		self.price    = price  
		self.quantity = quantity  

	def getDiscount(self):
		''' Returns the ID number of the athlete'''
		return self.price * Inventory.DISCOUNT

	def getPrice(self):
		''' Returns the ID number of the athlete'''
		return self.price

	def getName(self):
		''' Returns the name of the athlete'''
		return self.name

	def getQuantity(self):
		''' Returns the height of the athlete'''
		return self.quantity

	def purchaseItem(self, amount):
		''' Calculates the average time performance of the athlete'''

		if self.quantity >= amount :
			self.quantity -= amount
		
			if self.quantity ==0 :
				print "\n\n**Out of Stock**\n\n"
		
		else:
			print "\n\n**Out of Stock**\n\n"

		return self.quantity

	def returnItem(self, amount):
		''' Calculates the average time performance of the athlete'''

		self.quantity += amount
		
		print "\n\n %d items returned. We have %d now in stock \n\n" % (amount, self.quantity)

		return self.quantity


