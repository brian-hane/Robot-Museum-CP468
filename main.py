from aStar import aStar
from file import readFile, writeFile

inputFileName = raw_input("Enter the input file name (press Enter to default to \"input.txt\"): ") or "input.txt"
outputFileName = raw_input("Enter the output file name (press Enter to default to \"result.txt\"): ") or "result.txt"

enviro, startList, rendev = readFile(inputFileName)
print("Loaded data from {0}.".format(inputFileName))

solutions = aStar(enviro, startList, rendev)
print("Successfully computed solutions.")

writeFile("result.txt", rendev, solutions)
print("Wrote solutions to {0}.".format(outputFileName))

print("Exiting...")