"""
Sherman Yan
Assignment 7 - P7.3
"""

from sys import argv


##
# this is the main function.
# checks command line argment for input file and output file
# outputs the inputfile to output file with line number
#
def main():

    inputFileName = ""
    outputFileName = ""

    numFiles = 0  # Number of command line arguments that are files.

    # if there are more than the max arguments
    if not len(argv) == 3:
        usage()
        return

    # get the file names from the arguments
    for i in range(1, len(argv)):
        arg = argv[i]
        numFiles += 1
        if numFiles == 1:
            inputFileName = arg
        elif numFiles == 2:
            outputFileName = arg

    # Open the files.
    inputFile = openFile(inputFileName, 'r')
    outputFile = openFile(outputFileName, 'w')

    # write to output file with linecount
    lineCount = 1
    for line in inputFile:
        outputFile.write("/* " + str(lineCount) + " */ " + line + "\n")
        lineCount += 1

    # Close the files.
    inputFile.close()
    outputFile.close()


##
# opens files
# @param file name and file type
# @return file
#
def openFile(filename, fileType):

    try:
        file = open(filename, fileType)
        return file
    except IOError:
        print("File \"" + str(filename) + "\" opening error")


##
# prints the usage message
#
def usage():

    print("Usage: python3 P7.3.py infile outfile")


main()

