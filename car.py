import ride
class Car :
	def __init__(self):
		self.empty = True
		self.coords = (0,0)
		self.done = []
		#Ride Class
		self.rideOnProgress = None


	def addRide(self,ride"""Ride"""):
		self.rideOnProgress = ride


	def getCoords(self):
		return self.coords

	def move(self):
		pass

	
