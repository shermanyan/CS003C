"""
Final Project

Author: Sherman Yan, Josiah Aviles
"""

from cipherEncryption import CipherEncryption
from imageProcessor import ImageProcessing
from fileManager import OpenFile


def main():
    try:
        option = (input("Encrypt(E) or Decrypt(D)? ")).upper()  # Asks if encrypting or decrypting
        if not (option == 'D' or option == 'E'):  # Checks for valid input
            raise ValueError("Invalid type, try again.")
    except ValueError as error:
        print("ERROR:", str(error))
        return main()

    imageProcessor = ImageProcessing()
    imageProcessor.getImage()  # Gets and opens the image file
    key, code, msgLength = getKey()  # gathers key information from user
    imageProcessor.setStartStopStep(code[0], msgLength, code[1])  # Establishes where in the image to start, stop,
                                                                  # and how many pixels to skip

    if option == 'E':  # If encrypting
        fileManager = OpenFile()
        fileManager.openFile("Message", 'r')  # Opens the text file for reading
        message = fileManager.getFileData()  # Creates a single string of the contents from the file
        fileManager.closeFile()

        cryption = CipherEncryption(key, message)
        message = cryption.encode()  # Encrypts the message using the cipher
        imageProcessor.writeImageMessage(message)  # Writes the encrypted message into the image
        print("Message Encrypted\n" +       # Prints the key and two code values for the receiver of the image to use
              "Decryption Key: " + key + str(len(message)) + "\n" +
              "Code 1: " + str(code[0]) + "\n" +
              "Code 2: " + str(code[1]))

    else:   # If decrypting
        codedMessage = imageProcessor.getImageMessage()  # Retrieves the encrypted message from the image
        cryption = CipherEncryption(key, codedMessage)
        decodedMessage = cryption.decode()  # Decrypts the message using the cipher
        print("Decoded Message:", decodedMessage)  # Prints out the decrypted message

    # closes file in the end
    imageProcessor.closeFile()
    print("Thank You")


##
# Gets the key word, the length of the message, and the start/step values
# @param name the key word
# @return The valid key word, the start/step values, and the message length
#
def getKey(name=None):
    code = []
    msgLen = "0"
    try:
        while not name:
            name = input("Enter key: ")  # Asks for the key word
            for i in range(len(name)):
                if not name[i].isalnum():  # Checks if the key word only consists of letters and numbers
                    raise NameError("Invalid key format")
        while not len(code) == 2:
            code.append(int(input("Code " + str(len(code) + 1) + ": "))) # Appends the two code values into a list

        for i in name:
            if i.isnumeric():  # Gets the length of the message, which is also the stopping point, that is included
                msgLen += i    # with the key word
                name = name.replace(i, "")      # Removes the numbers after storing them

        return name, code, int(msgLen)

    except NameError as error:
        print("ERROR:", str(error))
        return getKey()
    except ValueError:
        print("ERROR: Code must be an integer")
        return getKey(name)


main()


"""
Sample Run
- Encryption Sample

Encrypt(E) or Decrypt(D)? e
Image file name: dog.bmp
Enter key: computerscienceimageprocessing
Code 1: 300
Code 2: 2000
Message file name: input.txt
Message Encrypted
Decryption Key: computerscienceimageprocessing143
Code 1: 300
Code 2: 2000
Thank You

- Decryption Sample

Encrypt(E) or Decrypt(D)? d
Image file name: dog.bmp
Enter key: computerscienceimageprocessing143
Code 1: 300
Code 2: 2000
Decoded Message: DONT STEP ON THE BROKEN GLASS FOR SOME UNFATHOMABLE REASON THE RESPONSE TEAM DIDNT CONSIDER A LACK OF MILK FOR MY CEREAL AS A PROPER EMERGENCY 
Thank You

"""
