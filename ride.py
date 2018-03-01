class Ride:
	def __init__(self,frm,to,earliestStart,latestFinish,rideNumber):
		self.frm = frm
		self.to = to
		self.earliestStart = earliestStart
		self.latestFinish = latestFinish
		self.rideNumber = rideNumber


	def from(self):
		return self.frm

	def to(self):
		return self.to

	def earliestStart(self):
		return self.earliestStart

	def latestFinish(self):
		return self.latestFinish
	
