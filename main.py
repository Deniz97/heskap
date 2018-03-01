import ride


r,c, vehicle_count, ride_conunt, bonus, time_steps = tuple(input().split(" "))

rides = []

for i in range(ride_conunt):
	start = [] #start location
	finish = [] #finish location
	start[0],start[1],finish[0],finish[1], earliest_start, latest_finish = tuple(input().split(" "))
	rides.append( ride.ride(start,finish,earliest_start,latest_finish) )







