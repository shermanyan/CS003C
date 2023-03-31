from io import SEEK_CUR
from fileManager import OpenFile


##
# Processes an image file
#
class ImageProcessing:
    ##
    # Constructs the image info and the info for retrieving the message
    #
    def __init__(self):
        self._imageFile = None
        self._startPixel = None
        self._numSkipPixels = None
        self._msgLength = None
        self._fileSize = None
        self._start = None
        self._width = None
        self._height = None
        self._scanlineSize = None
        self._padding = None

    ##
    # Opens the file for reading and writing in binary, gets the info, and checks if it is valid
    #
    def getImage(self):
        try:
            # get image file
            fileManager = OpenFile()
            fileManager.openFile("Image", 'rb+')
            self._imageFile = fileManager.getFile()
            # gets image information and checks image
            self._gatherImageInfo()
            self._checkImage()
        except TypeError as typeError:  # if any type errors occur, file format is incorrect.
            print("Error:", typeError)
            return self.getImage()

    ##
    # Checks if the file is a 24-bit true color image file
    #
    def _checkImage(self):
        if self._fileSize != (self._start + (self._scanlineSize + self._padding) * self._height):
            raise TypeError("Not a 24-bit true color image file.")

    ##
    # Retrieves image info
    #
    def _gatherImageInfo(self):
        self._fileSize = self._readInt(2)
        self._start = self._readInt(10)
        self._width = self._readInt(18)
        self._height = self._readInt(22)
        self._scanlineSize = self._width * 3
        self._padding = self._getPadding()

    ##
    # Sets the starting pixel, when to stop, and how many pixels to skip
    # @param start the position of the pixel to start reading/writing the message
    # @param stop the position of the last pixel to read/write
    # @param step the number of pixels to skip between reading/writing in characters
    #
    def setStartStopStep(self, start=0, stop=0, step=0):
        self._startPixel = (self._start - 1) + (int(start) * 3)
        self._numSkipPixels = step
        self._msgLength = stop

    ##
    # Retrieves the message encoded into the image
    # @return the encoded message
    #
    def getImageMessage(self):
        message = ""
        self._imageFile.seek(self._startPixel)
        currChar = self._imageFile.read(1)
        self._imageFile.seek(2, SEEK_CUR)

        # get message based on given message length
        while currChar and len(message) < self._msgLength:
            message += chr(*currChar)
            seekToNext = 0
            while seekToNext < self._numSkipPixels * 3:
                self._imageFile.seek(1, SEEK_CUR)
                if (self._imageFile.tell() - self._start) % (self._width * 3 + self._padding) < self._width * 3:
                    seekToNext += 1
            currChar = self._imageFile.read(1)
            self._imageFile.seek(2, SEEK_CUR)

        return message

    ##
    # Writes the encoded message into the image
    # @param the encrypted message
    #
    def writeImageMessage(self, message):
        characters = []
        # convert string to char list
        for i in range(len(message)):
            characters.append(message[i])

        self._imageFile.seek(self._startPixel)

        for i in range(len(characters)):
            # write the byte
            self._imageFile.write(bytes([ord(characters[i])]))
            # seek to next pixel
            self._imageFile.seek(2, SEEK_CUR)
            seekToNext = 0

            # seek to next pixel for given skips
            while seekToNext < self._numSkipPixels:
                self._imageFile.seek(3, SEEK_CUR)
                if (self._imageFile.tell() - self._start) % (self._width*3 + self._padding) < self._width * 3:
                    seekToNext += 1

    ##
    # Converts the info from the image header into readable integers
    # @param offset the position to move the file pointer to
    # @return The readable integer
    #
    def _readInt(self, offset):
        # Move the file pointer to the given byte within the file.
        self._imageFile.seek(offset)
        # Read the 4 individual bytes and build an integer. theBytes = imgFile.read(4)
        theBytes = self._imageFile.read(4)
        result = 0
        base = 1
        for i in range(4):
            result = result + theBytes[i] * base
            base = base * 256

        return result

    ##
    # Gets the padding at the end of the image
    # @return the number of extra bytes (padding)
    #
    def _getPadding(self):
        if self._scanlineSize % 4 == 0:
            padding = 0
        else:
            padding = 4 - self._scanlineSize % 4
        return padding

    ##
    # Closes the image file
    #
    def closeFile(self):
        self._imageFile.close()
