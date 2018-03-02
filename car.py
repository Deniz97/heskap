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
		#print("eklenecek ride: ",ride.rideNumber)
		#print(ride)
		#print("bos mu: ",self.isEmpty())
		if self.isEmpty():
			#Musteri 20 birimlik mesafeyi 10 birimde gitmeni istiyorsa
			self.rideOnProgress = ride	
			#print("setting ride ",ride.rideNumber," taken")
			ride.taken()
			#print("result: ",ride.isTaken)
			self.destination = ride.to
			#Arac earliestStarttan yakınsa araç bekliycek ve sonra gidicek yoksa arac direk gazliycak 
			self.movements = max(self.distanceBetweenRideAndCar(ride),ride.earliestStart) + self.distanceBetweenEndAndBeginning(ride)	
			return ride
		else:
			pass
			#print("isi olan bir araca gorev verildi." ,ride.frm , ride.to , ride.rideNumber)
	

	#Aracin yerini dondur.
	def getCoords(self):
		return self.coords

	def getDestination(self):
		#if self.
		pass
	
	"""Aracı n adım kadar ilerlet"""
	def move(self,n):
		#print(self.movements, "giris")
		if(self.rideOnProgress == None ):
			return

		if self.movements > n:
			self.movements -=n
		else:
			self.movements = 0
			self.coords = self.rideOnProgress.to
			"""
			Ride ın sadece numarası ekleniyor.
			Outputta sıkıntı çıkartabilir burası.
			"""
			self.done.append(str(self.rideOnProgress.rideNumber))
			self.rideOnProgress = None
		#print(self.movements, "cikis")
		
		
	def addBestRideGivenRides(self):
		#print("ava ride: ", self.availableRides)
		#print("ava notTaken ride: ", [ x for x in self.availableRides if not x[1].isTaken ])
		for r in self.availableRides:
			if not r[1].isTaken:
				return self.addRide(r[1])
				break
	

	def calculatePointsForRide(self,ride:Ride):
		pass
	
	def getMovement(self):
		return self.movements

	"""Aracın uygun olup olmadığını kontrol et."""
	"""Aracın yapıcağı hareket yoksa doğru varsa yanlış döndür."""
	
	def isEmpty(self):
		#print(self.movements, "aaa")
		if self.movements == 0:
			return True

		else:
			return False	
	#Rideın başıyla bitimi arasındaki mesafe 
	
	def distanceBetweenEndAndBeginning(self,ride):
		return abs(ride.fromm()[0]-ride.to[0]) + abs(ride.fromm()[1]-ride.to[1])

	#Araçla ride arasındaki mesafe
	def distanceBetweenRideAndCar(self,ride):
		rideCoords = ride.fromm()
		return abs(self.coords[0]-rideCoords[0]) + abs(self.coords[1] - rideCoords[1])
