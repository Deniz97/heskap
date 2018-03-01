import ride
class Car :
	def __init__(self):
		self.coords = (0,0)
		self.done = []
		#Ride Class
		self.rideOnProgress = None
		self.movements = 0 

	"""Yolu alıcak ve """
	def addRide(self,ride:Ride):
		self.rideOnProgress = ride	
		
	def getCoords(self):
		return self.coords

	"""Aracı n adım kadar ilerlet"""
	def move(self,n):
		if self.movements > n:
			self.movements -=n
		else:
			self.movements = 0
			
	

	"""Aracın uygun olup olmadığını kontrol et."""
	"""Aracın yapıcağı hareket yoksa doğru varsa yanlış döndür."""
	def isEmpty(self) -> bool:
		if self.movements == 0:
			return True

		else:
			return False

	
