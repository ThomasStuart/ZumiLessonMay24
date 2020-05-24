numRoutes = input("How many routes do I want to run :")
numRoutes = int(numRoutes)

startVertex = input("Starting Vertex: ")
endVertex   = input("Ending   Vertex: ")
routesArr = []

#do something here

for i in range(0, numRoutes):
    newRoute = [ ] #adjust this line
    
    first_item  = input("Starting Vertex: ") #changed or deleted ?
    second_item = input("Ending   Vertex: ") #changed or deleted ?
    
    
    routesArr.append(newRoute)


num = 0
while len(routesArr) > 0:
    print("Route ",num+1, ": ",end='')
    currRoute = routesArr.pop(0)  # route1  -> route2  -> route3

    print('(', end='')
    while len(currRoute) > 0:
        currItem = currRoute.pop(0)
        print(currItem + ',',end='')
    
    print(')', end='')
    num+=1
    print()
