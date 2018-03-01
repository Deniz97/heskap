from ride import Ride
class Car :
	def __init__(self):
		self.coords = (0,0)
		self.done = []
		#Ride Class
		self.rideOnProgress = None
		self.movements = 0 

	"""Yolu alıcak ve movementsı ayarlıcak"""
	def addRide(self,ride:Ride):
		if self.isEmpty():
			self.rideOnProgress = ride	
			
		else:
			print("İşi olan bir araca görev verildi." +ride.frm + self.to + self.rideNumber)
		
	def getCoords(self):
		return self.coords

	"""Aracı n adım kadar ilerlet"""
	def move(self,n):
		if self.movements > n:
			self.movements -=n
		else:
			self.movements = 0
			self.coords = self.rideOnProgress.to
			self.done.append(self.rideOnProgress)
			
		
	def setNextTAvaibleRide(self,T):
		pass

	def calculatePointsForRide(self,ride:Ride):
		pass
	
	def getMovement(self):
		return self.movements

	"""Aracın uygun olup olmadığını kontrol et."""
	"""Aracın yapıcağı hareket yoksa doğru varsa yanlış döndür."""
	def isEmpty(self) -> bool:
		if self.movements == 0:
			return True

		else:
			return False

	
