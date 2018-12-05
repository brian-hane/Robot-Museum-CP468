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


def writeFile(fileName, rendev, result):
    try:
        outputStream = open(fileName, "w+")
    except:
        raise Exception("Error writing to output file.")

    outputStream.write("Rendezvous Point: {0}\n\n".format(rendev))

    numRobots = len(result)
    for i in range(numRobots):
        outputStream.write("------Robot {0}------\n".format(i + 1))
        outputStream.write("Start location: {0}\n".format(result[i][0]))
        outputStream.write("Computed path: ")

        solution = result[i][1]
        if solution == None:
            outputStream.write("No solution found\n\n")
        else:
            numCoords = len(solution)
            for j in range(numCoords):
                outputStream.write("{0}".format(solution[j]))
                if (j != numCoords - 1):
                    outputStream.write(", ")
                    if ((j + 1) % 10 == 0):
                        outputStream.write("\n")
                else:
                    outputStream.write("\n\n")

    outputStream.close()
    return

if __name__ == '__main__':
    # test
    enviro, startList, rendev = readFile("input.txt")

    print(enviro)
    print(startList)
    print(rendev)
