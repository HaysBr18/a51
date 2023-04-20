
regX = []
regY = []
regZ = []

lenX = 19
lenY = 22
lenZ = 23


def fillRegisters(key):

    i = 0

    while (i < lenX):
        regX.insert(i, key[i])
        i += 1

    j = lenX

    while (j < lenX + lenY):
        regY.insert(j, key[j])
        j += 1

    k = lenX + lenY

    while (k < lenX + lenY + lenZ):
        regZ.insert(k, key[k])
        k += 1


    print(regX)
    print(len(regX))
    print(regY)
    print(len(regY))
    print(regZ)
    print(len(regZ))


def getMajority(x,y,z):

    if (x+y+z > 1):
        return 1
    else:
        return 0

#Generate the keystream for the key.
def getKeyStream():
    keyStream = ''

    while(len(keyStream) != 32):

        majority = getMajority(int(regX[8]), int(regY[10]), int(regZ[10]))
        
        #If any of the registers equal the majority, step the register.
        if(int(regX[8]) == majority):
            

        if(int(regY[10]) == majority):

        if(int(regZ[10]) == majority):



def main():
    key = "1010101010101010101110011001100110011001111100001111000011110000"
    keystream = " "

    fillRegisters(key)
    getKeyStream()


main()