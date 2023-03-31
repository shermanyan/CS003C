"""
Lab 9
Sherman Yan, Josiah Aviles, Junyan Wen
"""

INPUT_FILE_NAME = "babynames.txt"
BOY_OUTFILE = "boynames.txt"
GIRL_OUTFILE = "girlnames.txt"


##
# Main Function
# opens files and splits up the names and stores into new files
#
def main():

    inFile = openFile(INPUT_FILE_NAME, 'r')
    boyOutfile = openFile(BOY_OUTFILE, 'w')
    girlOutFile = openFile(GIRL_OUTFILE, 'w')

    processFile(inFile, boyOutfile, girlOutFile)

    inFile.close()
    boyOutfile.close()
    girlOutFile.close()

    boyFile = openFile(BOY_OUTFILE, 'r')
    girlFile = openFile(GIRL_OUTFILE, 'r')

    nameMatches = fileMatches(boyFile, girlFile)

    print("Matched names:", *nameMatches)

    boyFile.close()
    girlFile.close()

##
# opens files
# @param filename and file type
# @return file
#
def openFile(filename, fileType):

    try:
        file = open(filename, fileType)
        return file
    except IOError:
        print("File \"" + str(filename) + "\" opening error")


##
# process files and writes into a new file
# @param infile, files to write in, boyfile and girlfile
# @return none
def processFile(infile, boyFile, girlFile):

    line = infile.readline()

    while line:
        boy, girl = processLine(line)

        boyFile.write("%s %s\n" % (boy[0], boy[1]))
        girlFile.write("%s %s\n" % (girl[0], girl[1]))

        line = infile.readline()


##
# process line
# @param line to process
# @return boy and girl
#
def processLine(line):

    lineData = line.split()

    boys = (lineData[0], lineData[1])
    girls = (lineData[0], lineData[2])

    return boys, girls


##
# looks for matches in file1 and file 2
# @param file1 and file2
# @return matches
#
def fileMatches(file1, file2):

    nameMatches = []

    searchFile = file2.read().split()

    line = file1.readline()

    while line:
        lineData = line.split()
        if lineData[1] in searchFile:
            nameMatches.append(lineData[1])

        line = file1.readline()

    return nameMatches


main()

