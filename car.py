from ride import Ride
class Car :
	def __init__(self):
		self.coords = (0,0)
		self.done = []
		#Ride Class
		self.rideOnProgress = None
		self.movements = 0 
		self.destination = None
		self.availableRides = []

	"""Yolu alıcak ve movementsı ayarlıcak"""
	def addRide(self,ride:Ride):
		if self.isEmpty():
			#Musteri 20 birimlik mesafeyi 10 birimde gitmeni istiyorsa

			self.rideOnProgress = ride	
			ride.taken()
			self.destination = ride.destination()
			#Arac earliestStarttan yakınsa araç bekliycek ve sonra gidicek yoksa arac direk gazliycak 
			self.movements = max(self.distanceBetweenRideAndCar(ride),ride.earliestStart()) + self.distanceBetweenEndAndBeginning()	
		else:
			print("İşi olan bir araca görev verildi." +ride.frm + self.to + self.rideNumber)
	

	#Aracin yerini dondur.
	def getCoords(self):
		return self.coords

	def getDestination(self):
		#if self.
		pass
	
	"""Aracı n adım kadar ilerlet"""
	def move(self,n):
		if self.movements > n:
			self.movements -=n
		else:
			self.movements = 0
			self.coords = self.rideOnProgress.to
			"""
			Ride ın sadece numarası ekleniyor.
			Outputta sıkıntı çıkartabilir burası.
			"""
			self.done.append(ride.rideNumber)
		
		
	def addBestRideGivenRides(self):
		for r in self.availableRides:
			if not r.isTaken:
				self.addRide(r)
	

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
	#Rideın başıyla bitimi arasındaki mesafe 
	def distanceBetweenEndAndBeginning(self,ride):
		return abs(ride.from()[0]-ride.to()[0]) + abs(ride.from()[1]-ride.to()[1])

	#Araçla ride arasındaki mesafe
	def distanceBetweenRideAndCar(self,ride):
		rideCoords = ride.from()
		return abs(self.coords[0]-rideCoords[0]) + abs(self.coords[1] - rideCoords[1])
