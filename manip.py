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
		print("File does not have that many lines.")
		sys.exit(2)
	




file.close()
file = open(sys.argv[len(sys.argv)-1], 'w')
file.write(newText)
file.close()
