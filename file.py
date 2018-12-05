"""  
-------------------------------------------------------  
file.py
-------------------------------------------------------  
Author:  Brian Hane, Sumeet Jhand
_updated_ ="2018-12-04"
-------------------------------------------------------  
"""

def readFile(fileName):
    startList = []
    enviro = []
    try:
        inputStream = open(fileName, "r")
    except:
        raise Exception("Could not locate input file {0}.".format(fileName))

    # room layout and other info
    curr = inputStream.readline().split()
    roomHeight = int(curr[0])
    roomWidth = int(curr[1])

    # robot count
    numBots = int(inputStream.readline())

    # coordinates of robots
    for _ in range(0, numBots):
        botCoords = inputStream.readline().split()
        location = []
        for coord in botCoords:
            location.append(int(coord))
        startList.append(location)

    # rendezvous location
    rendev = []
    rendevList = inputStream.readline().split()
    rendev.append(int(rendevList[0]))
    rendev.append(int(rendevList[1]))

    # read layout of room points
    for _ in range(0, roomHeight):
        curr = inputStream.readline()
        row = []
        for c in curr:
            if c == '1' or c == '0':
                row.append(int(c))
        enviro.append(row)

    inputStream.close()
    return enviro, startList, rendev


def writeFile(result):
    invalidFile = True
    while invalidFile:
        try:
            filename = input("Enter output file name:")
            outputStream = open(filename, "w", encoding="utf-8")
            for x in result:
                outputStream.writelines(str(x))
                outputStream.write("\n")
            invalidFile = False
        except:
            print("File not found")
    outputStream.close()
    return

if __name__ == '__main__':
    # test
    enviro, startList, rendev = readFile("input.txt")

    print(enviro)
    print(startList)
    print(rendev)

    arr = [100000001,
        100000010,
        100000010,
        100000010,
        100000010,
        100000010]
    writeFile(arr)
