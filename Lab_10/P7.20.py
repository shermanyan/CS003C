"""
Sherman Yan, Josiah Aviles, Junyan Wen
"""

from sys import argv


##
# this is the main function.
# takes care of the command line inputs and encodes or decodes
#
def main():
    key = ""
    inFile = ""
    outFile = ""
    decode = False
    files = 0  # Number of command line arguments that are files.

    for i in range(1, len(argv)):
        arg = argv[i]
        if arg[0] == "-":
            # It is a command line option.
            option = arg[1]
            if option == "k":  # it is a key
                key = arg[2:].upper()
            elif option == "d":  # decode
                decode = True
            elif option == "e":  # encode
                decode = False
            else:
                usage()
                return
        else:
            # It is a file name.
            files += 1
            if files == 1:
                inFile = arg
            elif files == 2:
                outFile = arg

    # There must be two files.
    if not key:
        usage()
        return
    if files != 2:
        usage()
        return

    # Open the files.
    inputFile = open(inFile, "r")
    outputFile = open(outFile, "w")

    if decode:
        for line in inputFile:  #reads every line in file
            newLine = decrypt(line.upper(), key)
            outputFile.write(newLine)
    else:  # encode
        for line in inputFile:
            newLine = encrypt(line.upper(), key)
            outputFile.write(newLine)

    # Close the files.
    inputFile.close()
    outputFile.close()


##
# generates the key from the keyword
# @param the key
# @return the new key
#
def genKey(key):
    key = key.upper()
    newKey = ""

    for char in range(len(key)):
        if key[char] not in newKey:
            newKey += key[char]

    for i in range(26):
        if chr(90 - i) not in newKey:
            newKey += chr(90 - i)

    return newKey


##
# encrypts the line with given key
# @param line, key
# @return the encoded line
#
def encrypt(line, key):

    encoded = ""
    crypt = genKey(key)

    for char in line:
        encoded += crypt[(ord(char)-65)]    # convert the character to an index
                                            # use index to find the corresponding letter in the key

    return encoded


##
# decrypts the line with given key
# @param line, key
# @return the decoded key
#
def decrypt(line, key):

    encoded = ""
    crypt = genKey(key)

    for char in line:  # for every character in the line
        encoded += chr(65 + crypt.index(char))  # find the index of the char in the key
                                                # use index to find the corresponding letter

    return encoded


##
# prints the usage message
#
def usage():

    print("Usage: python P7.20.py -[d][e] -kKEY infile outfile")


main()

