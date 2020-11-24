#Andrew Koehn
#11/23/20
#Project 3
import sys

if len(sys.argv) == 1:
	print("Usage: python manip.py <OPERATION> [PARAMETERS] <FILE>")
	sys.exit(1)

if sys.argv[1] != "-a" and sys.argv[1] != "-r" and sys.argv[1] != "-f" and sys.argv[1] != "-c" and sys.argv[1] != "-t":
	print("Operation not recognized. Try -a, -r, -f, -c, or -t")
	sys.exit(2)
	
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

'''
elif sys.argv[1] == "-r":
	if len(sys.argv) != 4:
		print("Usage: python manip.py -r <LINE NUMBER> <FILE>")
		sys.exit(1)
	elif sys.argv[
	lineNumber = 1
'''
	




file.close()
file = open(sys.argv[len(sys.argv)-1], 'w')
file.write(newText)
file.close()
