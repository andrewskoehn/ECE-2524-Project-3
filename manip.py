#################
# Andrew Koehn
# 12/1/20
# Project 3

# Modules
import sys
import re

# Usage error handling
if len(sys.argv) < 4:
	print("Usage: python manip.py <OPERATION> <PARAMETERS> <FILE>")
	sys.exit(1)

# File error handling
test = re.search("\.", sys.argv[len(sys.argv)-1])
if test == None:
	print("Usage: python manip.py <OPERATION> <PARAMETERS> <FILE>")
	sys.exit(1)
try:
	file = open(sys.argv[len(sys.argv)-1], 'r')
except OSError:
	print("File does not exist or cannot be opened.")
	sys.exit(3)

# Append (-a) implementation
if sys.argv[1] == "-a":
	# Usage error handling
	if len(sys.argv) != 4:
		print("Usage: python manip.py -a <STRING> <FILE>")
		sys.exit(1)
	newText = file.read()
	newText += sys.argv[2]

# Remove (-r) implementation
elif sys.argv[1] == "-r":
	# Usage error handling
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
	# Read through file and skip appropriate line
	for line in file:
		if lineNumber == num:
			found = True
			lineNumber += 1
		else:
			lineNumber += 1
			newText += line
	# Range error handling
	if not found:
		print("File does not contain that many lines.")
		sys.exit(2)

# Find/replace (-f) implementation
elif sys.argv[1] == "-f":
	# Usage error handling
	if len(sys.argv) != 5:
		print("Usage: python manip.py -f <FIND> <REPLACE> <FILE>")
		sys.exit(1)
	find = sys.argv[2]
	replace = sys.argv[3]
	newText = file.read()
	oldText = newText
	# Use str.replace built-in function
	newText = newText.replace(find, replace)
	# No occurrence handling
	if newText == oldText:
		print("No occurrences of \""+find+"\" to be replaced.")
		sys.exit(2)

# Count (-c) implementation
elif sys.argv[1] == "-c":
	# Usage error handling
	if len(sys.argv) != 4:
		print("Usage: python manip.py -c <STRING> <FILE>")
		sys.exit(1)
	string = sys.argv[2]
	text = file.read()
	# Use str.count built-in function
	numOccurrences = text.count(string)
	# No occurrence handling
	if numOccurrences == 0:
		print("No occurrences of \""+string+"\" found.")
		sys.exit(2)
	else:
		print(numOccurrences,"occurrence(s) of \""+string+"\" found.")
		sys.exit(0)

# Comment (-t) implementation
elif sys.argv[1] == "-t":
	# Usage error handling
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
	# Read through file and add comment character at beginning of appropriate lines
	for line in file:
		if lineNumber >= start and lineNumber <= end:
			found = True
			newText += comment+line
			lineNumber += 1
		else:
			newText += line
			lineNumber += 1
	# Range error handling
	if not found or lineNumber < end+1:
		print("File does not contain the given line range.")
		sys.exit(2)

# Usage error handling
else:
	print("Operation not recognized. Try -a, -r, -f, -c, or -t")
	sys.exit(2)

file.close()

# Update file with changes
file = open(sys.argv[len(sys.argv)-1], 'w')
file.write(newText)
file.close()

#FINAL