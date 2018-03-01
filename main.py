import ride
import mapim
import car
import driver


def setNextTAvailableRides(car,rides,current_time,look_ahead_time):
	reduced_rides = [ x for x in rides if x.earliestStart < current_time + look_ahead_time ]
	
	reduced_rides.sort( key = lambda x: x.calcScore4Car(car,current_time)[0], reverse=True )

	car.availableRides = reduced_rides



r,c, vehicle_count, ride_conunt, bonus, time_steps = tuple(input().split(" "))

##pezevenk müsterileri filterla
##


#obivous
look_ahead_time_count = 100

rides = []
cars = []

#set map
grid = mapim.mapim(r,c)

#append rides
for i in range(ride_conunt):
	start = [] #start location
	finish = [] #finish location
	start[0],start[1],finish[0],finish[1], earliest_start, latest_finish = tuple(input().split(" "))
	
	#turn to ints and tuples
	start[0] = int(start[0])
	start[1] = int(start[1])
	finish[0] = int(finish[0])
	finish[1] = int(finish[1])
	start = tuple(start)
	finish = tuple(finish)
	earliest_start = int(earliest_start)
	latest_finish = int(latest_finish)

	rides.append( ride.ride(start,finish,earliest_start,latest_finish, i, bonus) ) #i is "ride number"

#append initial rides
for i in range(vehicle_count):
	cars.append( car.Car() )




for t in range(time_steps):
	
	reduced_cars = [ x for x in cars if x.isEmpty() ]

	for c in reduced_cars:
		setNextTAvailableRides(c,rides,t,look_ahead_time_count)

	cars.sort( key = lambda x: x.availableRides[0],reverse=True )
	for c in reduced_cars:
		#below method will:
		#add c it's biggest point ride, if it is not already taken
		#if taken move to the next ride in its respective availableRides list
		#then mark the added ride "isTaken=True"
		c.addBestRideGivenRides()

	#maybe make it possible to reassign rides until it goes to start position

	#


	#maybe re-assign drives here

	###

	for c in reduced_cars:
		#move one step
		c.move(1)

	t+=1



for c in cars:
	print(assignedRides)







	







