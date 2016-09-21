import math
def multilateration():
    xA = 0.5
    yA = 0
    xB = -0.5
    yB = 0
    #xC = 0
    #yC = 1
    min = -250
    max = 250
    average = 0
    close = 1000000
    closestX = 0
    closestY = 0
    ac = float(raw_input('What is the TDoA between points C and A? [Must be in decimal form] '))
    bc = float(raw_input('What is the TDoA between points C and B? [Must be in decimal form] '))
    #convert time into meters using speed of sound [1481m/s]
    distanceac = 1481*ac
    distanceac = round(distanceac, 15)
    distancebc = 1481*bc
    distancebc = round(distancebc, 15)
    h = min
    k = min
    while h < max:
        h += 0.1
        #print "h: " + str(h)
        while k < max:
            k += 0.1
            #print "k: " + str(k)
            #c = math.sqrt((xC-h)*(xC-h)+(yC-k)*(yC-k))
            b = math.sqrt((xB-h)*(xB-h)+(yB-k)*(yB-k))-distancebc
            a = math.sqrt((xA-h)*(xA-h)+(yA-k)*(yA-k))-distanceac
            #c = round(c, 5)
            #print c
            b = round(b, 15)
            #print b
            a = round(a, 15)
            #print a
            average = abs(b-a)
            if average < close:
                closestX = h
                closestY = k
                close = average
        k = min
    print close
    response = "(" + str(closestX) + "," + str(closestY) + ")"
    return response
            

        
    
    