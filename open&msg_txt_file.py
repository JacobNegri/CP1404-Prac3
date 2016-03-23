
## Open a text file and print using information from the file

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()