##
# Opens files and gets file information
#
class OpenFile:
    ##
    # Constructs a file holder
    #
    def __init__(self):
        self._file = None

    ##
    # Opens a file
    # @param fileType Image file or text file
    # @param fileReadType read, write, or both (or binary)
    #
    def openFile(self, fileType, fileReadType):
        filename = str(input(fileType + " file name: "))
        try:  # try opening file
            file = open(filename, fileReadType)
            self._file = file
        except IOError:  # if file opening fails, prompt error and ask for file again
            print("ERROR: File \"" + filename + "\" opening error, try again.")
            return self.openFile(fileType, fileReadType)

    ##
    # Returns the file
    # @return the file
    #
    def getFile(self):
        return self._file

    ##
    # Creates a list of words from each line in file and reconstructs it into one string
    # @return The string of words
    #
    def getFileData(self):
        lineData = []
        data = ""
        for line in self._file:
            lineData.append(line.strip())
        for i in lineData:
            data += str(i) + ' '
        return data[:-1]

    ##
    # Closes the file
    #
    def closeFile(self):
        self._file.close()

