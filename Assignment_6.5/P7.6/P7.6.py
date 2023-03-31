"""
Sherman Yan
Assignment 7 - P7.6
"""

from sys import argv


##
# this is the main function.
# Search files in argument for target from argument
# @return usage() if invalid command line arguments
#
def main():

    inputFileNames = []

    if not len(argv) >= 2:
        usage()
        return

    searchTarget = argv[1]

    for i in range(2, len(argv)):
        inputFileNames.append(str(argv[i]))

    print("Searching for \"" + searchTarget + "\" in:", *inputFileNames)

    # Open the files.
    inputFiles = []
    for i in range(len(inputFileNames)):
        inputFiles.append(openFile(str(inputFileNames[i]), 'r'))

    # print results of search
    for i in range(len(inputFiles)):
        print(inputFileNames[i] + ":", *searchFile(inputFiles[i], searchTarget))

    # Close the files.
    for i in range(len(inputFiles)):
        inputFiles[i].close()


##
# searches file for the target
# @param file, target
# @return all lines from the file that have the target
#
def searchFile(file, target):
    lineMatches = []

    for line in file:
        if target in line:
            lineMatches.append(line.replace('\n', ""))

    return lineMatches


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

    print("Usage: python3 P7.3.py searchFiles [searchFiles] [searchFiles] [searchFiles]")


main()


"""
Sample Run
shermanyan@sMac P7.6 % python3 P7.6.py his fileOne.txt fileTwo.txt fileThree.txt
Searching for "his" in: fileOne.txt fileTwo.txt fileThree.txt
fileOne.txt: Plans for this weekend
fileTwo.txt: his parents wouldn’t let him sell
fileThree.txt: his little sister at the garage sale.

"""