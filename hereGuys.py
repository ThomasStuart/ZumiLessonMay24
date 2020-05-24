numRoutes = input("How many routes do I want to run :")
numRoutes = int(numRoutes)

startVertex = input("Starting Vertex: ")
endVertex   = input("Ending   Vertex: ")
routesArr = []

#TODO:: add 1 line code here 

for i in range(0, numRoutes):
    newRoute = [ ] #TODO:: add something in the brackets 
    
    first_item  = input("Starting Vertex: ") # TODO:: EDIT delete or keep ?
    second_item = input("Ending   Vertex: ") # TODO::  EDIT delete or keep ?
    
    
    routesArr.append(newRoute)


num = 0
while len(routesArr) > 0:
    print("Route ",num+1, ": ",end='')
    currRoute = routesArr.pop(0)  

    print('(', end='')
    while len(currRoute) > 0:
        currItem = currRoute.pop(0)
        print(currItem + ',',end='')
    
    print(')', end='')
    num+=1
    print()

#Example 1      user requested to make 3 routes 
#----------
# the program right now 
# Route 1:  (input=a, input=b) 
# Route 2:  (input=b, input=c)
# Route 3:  (input=c, input=d)

#Goal:
# Route 1:  (input=a, input=b) 
# Route 2:  (b, input=c)
# Route 3:  (c, input=d)


#done with input
#----------
# Route 1: (a,b)
# Route 1: (b,c)
# Route 1: (c,d)


#Example 2     
#----------
# 2 routes
# (input= x,input= y)
# (input=y,input=z)   # had to input both

#goal
# (input= x,input= y)
# (y, input=z)        # only 1 input 


#done with input
#----------
# (x,y)
# (y,z)
