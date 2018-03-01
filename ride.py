class Ride:
	def __init__(self,frm,to,earliestStart,latestFinish):
		self.frm = frm
		self.to = to
		self.earliestStart = earliestStart
		self.latestFinish = latestFinish


	def from(self):
		return self.frm

	def to(self):
		return self.to

	def earliestStart(self):
		return self.earliestStart

	def latestFinish(self):
		return self.latestFinish
	
