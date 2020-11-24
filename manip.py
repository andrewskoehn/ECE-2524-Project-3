#Andrew Koehn
#11/23/20
#Project 3
import sys

if len(sys.argv) == 1:
	print("Usage: python manip.py <OPERATION> [PARAMETERS] <FILE>:")
	sys.exit(1)

if sys.argv[1] != "-a" and sys.argv[1] != "-r" and sys.argv[1] != "-f" and sys.argv[1] != "-c" and sys.argv[1] != "-t":
	print("Operation not recognized. Try -a, -r, -f, -c, or -t")
	sys.exit(2)