class Ride:
	def __init__(self,frm,to,earliestStart,latestFinish,rideNumber):
		self.frm = frm
		self.to = to
		self.earliestStart = earliestStart
		self.latestFinish = latestFinish
		self.rideNumber = rideNumber
		self.isTaken = False

	def from(self):
		return self.frm

	def to(self):
		return self.to

	def earliestStart(self):
		return self.earliestStart

	def latestFinish(self):
		return self.latestFinish

	def rideNumber(self):
		return self.rideNumber
	
	#Rideın alınıp alınmadığını gösteriyor.
	def taken(self):
		self.isTaken = True
