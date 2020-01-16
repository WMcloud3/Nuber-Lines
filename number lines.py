def main():
    userFileName = input("Please enter file name: ")

    fileToReadFrom = open(userFileName, "r")

    line = fileToReadFrom.readline()

    lineNumber = 1

    while line != "":
        print(str(lineNumber) + ":", line.rstrip("\n"))
        line = fileToReadFrom.readline()
        lineNumber = lineNumber + 1

    print ()
    print (lineNumber - 1)

main()

