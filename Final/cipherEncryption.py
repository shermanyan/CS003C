##
# Encrypts and decrypts messages
# @param key and message, both default to none
#
class CipherEncryption:

    ##
    # Constructs an empty key and empty message
    #
    def __init__(self, key=None, message=None):
        self._message = message.upper()
        self._key = key.upper()
        self._key = self._genKey(self._key)

    ##
    # Generates key from the keyword
    # @param message to generate key for
    # @return generated key
    #
    def _genKey(self, message):
        newKey = ""
        for char in range(len(message)):
            if message[char] not in newKey:
                newKey += message[char]

        for i in range(26):
            if chr(90 - i) not in newKey:
                newKey += chr(90 - i)

        return newKey

    ##
    # Encrypts the line with given key
    # @return the encoded line
    #
    def encode(self):
        encoded = ""

        for char in self._message:
            if str(char).isalpha():
                encoded += self._key[(ord(char) - 65)]
            elif str(char).isspace():
                encoded += " "
        return encoded

    ##
    # Decrypts the line with given key
    # @return the decoded key
    #
    def decode(self):
        decoded = ""
        for char in self._message:
            if char in self._key:
                decoded += chr(65 + self._key.index(char))
            elif str(char).isspace():
                decoded += " "
        return decoded
