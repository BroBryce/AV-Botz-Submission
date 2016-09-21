import math
def distance(textFile):

    file = open(textFile, "r")
    x,y,z = [], [], []
    for f in file:
        row = f.split()
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
    a = 0
    over200 = 0
    values = []
#   print (len(x))
    while len(x) > a:
        xValue = int(x[a])
        yValue = int(y[a])
        zValue = int(z[a])
        distance = math.sqrt((xValue*xValue)+(yValue*yValue)+(zValue*zValue))
        distance = int(distance)
#       print (distance)
        if distance > 200:
            over200 += 1
        values.append(distance)
        a += 1
    values.append(over200)
#   print (values)
    endFile = open('text.out.txt', 'w')
    for item in values:
        endFile.write("%s\n" % item)