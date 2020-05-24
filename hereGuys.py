def isQuitCommand( string ):
    for character in string:
        if character == 'Q' or character == 'q':
            return True
    return False

routesArr = []


numRoutes = input("How many routes do I want to run :")
numRoutes = int(numRoutes)


startVertex = input("Starting Vertex: ")
endVertex   = input("Ending   Vertex: ")


routesArr.append([startVertex, endVertex])

for i in range(0, numRoutes-1):
    startVertex = endVertex
    endVertex = input("Next Vertex: ")
    # do something here 
    
    routesArr.append([startVertex, endVertex])


print()    
print()

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


