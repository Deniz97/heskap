import ride
import car
from functools import cmp_to_key

def setNextTAvailableRides(car,rides,current_time,look_ahead_time):
    
    reduced_rides = [ (x.calcScore4Car(car, current_time), x) for x in rides if (x.earliestStart < current_time + look_ahead_time) and (not x.isTaken) ]
    #print("in tavailabe red rides: ",reduced_rides)
    reduced_rides.sort( key = lambda x: x[0], reverse=True )

    car.availableRides = reduced_rides


def cmpCar(car1, car2):
    until = min(len(car1.availableRides), len(car2.availableRides))
    for i in range(until):
        if car1.availableRides[i] == car2.availableRides[i]:
            continue
        return car1.availableRides[i] > car2.availableRides[i]

    #print("Buraya gelmemeliydik xd")

    return True 
    

r,c, vehicle_count, ride_conunt, bonus, time_steps = tuple(input().split(" "))
ride_conunt = int(ride_conunt)
bonus = int(bonus)
vehicle_count = int(vehicle_count)
time_steps = int(time_steps)
##pezevenk müsterileri filterla
##


#obivous
look_ahead_time_count = 100

rides = []
cars = []

#set map
#grid = mapim.mapim(r,c)

#append rides
for i in range(ride_conunt):
    start = [0,0] #start location
    finish = [0,0] #finish location
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

    rides.append( ride.Ride(start,finish,earliest_start,latest_finish, i, bonus) ) #i is "ride number"

#append initial rides
for i in range(vehicle_count):
    cars.append( car.Car() )




for t in range(time_steps):

    if len(rides) == 0:
        break
    #print()
    #print("an iteration starts    ", t)

    
    #print("cars: ",cars)
    
    
    reduced_cars = [ x for x in cars if x.isEmpty() ]
    #print("red cars: ", reduced_cars)

    for c in reduced_cars:
        setNextTAvailableRides(c,rides,t,look_ahead_time_count)

    #print(cars[0].availableRides[0], "bbb")

    sorted(cars, key = cmp_to_key(cmpCar) )


    card_to_add_ride = [ x for x in reduced_cars if len(x.availableRides) != 0 ]

    card_to_add_ride.sort( key = lambda x: x.availableRides[0][0],reverse=True )
    for c in card_to_add_ride:
        #below method will:
        #add c it's biggest point ride, if it is not already taken
        #if taken move to the next ride in its respective availableRides list
        #then mark the added ride "isTaken=True"
        #print("bir araca bir ride verilecek: ",c)
        
        added_ride = c.addBestRideGivenRides()
        
        if(added_ride != None):
        	rides.remove(added_ride)

    #maybe make it possible to reassign rides until it goes to start position

    #


    #maybe re-assign drives here

    ###

    for c in cars:
        #move one step
        c.move(1)

    t+=1


#print("finished")
for i in range(len(cars)):
    
    print(i+1," ".join(cars[i].done))







    







