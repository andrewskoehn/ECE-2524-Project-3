#Andrew Koehn
#11/23/20
#Project 3
import sys
import re


if len(sys.argv) < 4:
	print("Usage: python manip.py <OPERATION> [PARAMETERS] <FILE>")
	sys.exit(1)

if sys.argv[1] != "-a" and sys.argv[1] != "-r" and sys.argv[1] != "-f" and sys.argv[1] != "-c" and sys.argv[1] != "-t":
	print("Operation not recognized. Try -a, -r, -f, -c, or -t")
	sys.exit(2)

test = re.search("\.", sys.argv[len(sys.argv)-1])
if test == None:
	print("Usage: python manip.py <OPERATION> [PARAMETERS] <FILE>")
	sys.exit(1)

try:
	file = open(sys.argv[len(sys.argv)-1], 'r')
except OSError:
	print("File does not exist or cannot be opened.")
	sys.exit(3)



if sys.argv[1] == "-a":
	if len(sys.argv) != 4:
		print("Usage: python manip.py -a <STRING> <FILE>")
		sys.exit(1)
	newText = file.read()
	newText += sys.argv[2]



elif sys.argv[1] == "-r":
	if len(sys.argv) != 4 or not sys.argv[2].isnumeric():
		print("Usage: python manip.py -r <LINE NUMBER> <FILE>")
		sys.exit(1)
	num = int(sys.argv[2])
	if num == 0:
		print("<LINE NUMBER> must be > 0.")
		sys.exit(2)
	newText = ""
	lineNumber = 1
	found = False
	for line in file:
		if lineNumber == num:
			found = True
			lineNumber += 1
		else:
			lineNumber += 1
			newText += line
	if not found:
		print("File does not contain that many lines.")
		sys.exit(2)



elif sys.argv[1] == "-f":
	if len(sys.argv) != 5:
		print("Usage: python manip.py -f <FIND> <REPLACE> <FILE>")
		sys.exit(1)
	find = sys.argv[2]
	replace = sys.argv[3]
	newText = file.read()
	oldText = newText
	newText = newText.replace(find, replace)
	if newText == oldText:
		print("No occurences of \""+find+"\" were found.")
		sys.exit(2)



elif sys.argv[1] == "-c":
	if len(sys.argv) != 4:
		print("Usage: python manip.py -c <STRING> <FILE>")
		sys.exit(1)
	string = sys.argv[2]
	newText = file.read()
	numOccurences = newText.count(string)
	if numOccurences == 0:
		print("No occurences of \""+string+"\" found.")
		sys.exit(2)
	else:
		print(numOccurences,"occurence(s) of \""+string+"\" found.")



elif sys.argv[1] == "-t":
	if len(sys.argv) != 6 or not sys.argv[3].isnumeric() or not sys.argv[4].isnumeric():
		print("Usage: python manip.py -t <COMMENT> <START> <END> <FILE>")
		sys.exit(1)
	start = int(sys.argv[3])
	end = int(sys.argv[4])
	comment = sys.argv[2]
	if start == 0:
		print("<START> must be > 0.")
		sys.exit(2)
	newText = ""
	lineNumber = 1
	found = False
	for line in file:
		if lineNumber >= start and lineNumber <= end:
			found = True
			newText += comment+line
			lineNumber += 1
		else:
			newText += line
			lineNumber += 1
	if not found or lineNumber < end+1:
		print("File does not contain the given line range.")
		sys.exit(2)
	
	




file.close()
file = open(sys.argv[len(sys.argv)-1], 'w')
file.write(newText)
file.close()
