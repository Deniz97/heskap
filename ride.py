class Ride:
	def __init__(self,frm,to,earliestStart,latestFinish,rideNumber, bonus):
		self.frm = frm
		self.to = to
		self.earliestStart = earliestStart
		self.latestFinish = latestFinish
		self.rideNumber = rideNumber
		self.isTaken = False

		tmpScore = abs(frm[0] - to[0]) + abs(frm[1] - to[1]) ## it is really temp
		self.score = (tmpScore, tmpScore + bonus)
                # a tuple of score w/o bonus and score w/ bonus

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
    
        # return tuple of rate w/o bonus & w/ bonus & rideNumber
    def calcScore4Car(self, car, curTime):
        penalty = abs(self.frm[0] - car.coords[0]) + abs(self.frm[1] - car.coords[1])
               
        if curTime > self.earliestStart:
            return (self.score[0] / penalty, self.score[0] / penalty, self.rideNumber)
        else:
            return (self.score[1] / penalty, self.score[1] / penalty, self.rideNumber)
        

                    


