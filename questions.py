
def main() :
    filename = input("Please enter the file name: ")

    # Open as a binary file for reading and writing.
    imgFile = open(filename, "rb+")

    # Extract the image information.
    fileSize = readInt(imgFile, 2)
    start = readInt(imgFile, 10)
    width = readInt(imgFile, 18)
    height = readInt(imgFile, 22)
    # Scan lines must occupy multiples of four bytes.
    scanlineSize = width * 3
    if scanlineSize % 4 == 0 :
        padding = 0
    else :
        padding = 4 - scanlineSize % 4

    print("File Size:", fileSize)
    print("Offset:", start)
    print("Width:", width)
    print("Height:", height)
    print("Padding:", padding)
    imgFile.seek(start)
    print("First 3 bytes:", *imgFile.read(3))

    imgFile.close()

def readInt(imgFile, offset) :
    # Move the file pointer to the given byte within the file.
    imgFile.seek(offset)
    # Read the 4 individual bytes and build an integer.
    theBytes = imgFile.read(4)
    result = 0
    base = 1
    for i in range(4) :
        result = result + theBytes[i] * base
        base = base * 256

    return result


main()