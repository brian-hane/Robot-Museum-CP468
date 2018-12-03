"""  
-------------------------------------------------------  
file.py
[program description]
-------------------------------------------------------  
Author:  Brian Hane 
ID:      150571750  
Email:   hane1750@mylaurier.ca 
_updated_ ="2018-12-01"
-------------------------------------------------------  
"""


def readFile():
    invalidFile = True
    #rendezLocation = None
    robotLocations = []
    roomPoints = []
    while invalidFile:
        # currently doesnt work with input filenames, requires hard coded
        filename = input("Enter layout file name:")
        print(filename)
        #filename = "input_test.txt"
        try:
            inputStream = open(filename, "r", encoding="utf-8")
            invalidFile = False
        except:
            print("File not found")

        # room layout and other info
        curr = inputStream.readline().split()
        roomHeight = int(curr[0])
        roomWidth = int(curr[1])
        # robot count
        numBots = int(inputStream.readline())

        # coordinates of robots
    for x in range(0, numBots):
        curr = inputStream.readline().split()
        #robotLocations.append(int(curr[0]), int(curr[1]), x)
        robotLocations.append(int(curr[0]) + int(curr[1]) + x)
    # rendezvous location
        curr = inputStream.readline().split()
        #rendezLocation.append(int(curr[0]) + int(curr[1]) + numBots)
        rendezLocation = int(curr[0])
        rendezLocation = rendezLocation + int(curr[0])
        rendezLocation = rendezLocation + numBots
    # read layout of room points
    for x in range(0, roomHeight):
        curr = list(inputStream.readline())
        roomPoints.append(curr)

    inputStream.close()
    return roomHeight, roomWidth, numBots, rendezLocation, robotLocations


def writeFile(result):
    invalidFile = True
   # filename = "output_test.txt"
  #  outputStream = open("output_test.txt", "w", encoding="utf-8")

    while invalidFile:
        try:
            filename = input("Enter output file name:")
            if filename == "output_test.txt":
                print("true")
            else:
                print("fuck")
            outputStream = open("filename", "w", encoding="utf-8")

            for x in result:
                outputStream.write(str(x))
                outputStream.write("\n")
                print("file")
            invalidFile = False
        except:
            print("File not found")

    outputStream.close()
    return


# test
#roomHeight, roomWidth, numBots, rendezLocation, robotLocations = readFile()
arr = [100000001,
       100000010,
       100000010,
       100000010,
       100000010,
       100000010]
writeFile(arr)
