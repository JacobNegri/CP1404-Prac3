
## Ask user for name and write to file

outFile = open("name.txt", "w")
name = input("Enter your name:")
outFile.write(name)
outFile.close