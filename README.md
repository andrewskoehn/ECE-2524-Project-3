# ECE-2524-Project-3
For Project 3, I developed a Python program called manip.py that
manipulates files via command-line arguments.

The program runs via Python and is executed by calling
"python manip.py &lt;OPERATION> &lt;PARAMETERS> &lt;FILE>" in a terminal
where OPERATION is a flag specifying the intended operation to perform on
FILE and PARAMETERS vary depending on which operation is selected.

The program can modify any file type that can be edited in a text editor.
Common file extensions modifiable by manip.py include .txt, .cpp, .py, and .sh.

OPERATIONS

- Append (-a): appends the given string to the end of the given file (does not insert
	a newline character)
	
	USAGE: python manip.py -a &lt;STRING> &lt;FILE>  
	Example: python manip.py -a while test.py  
	Example: python manip.py -a "\nthis adds a newline" myFile.cpp  
	
- Remove (-r): removes the given line from the given file
	
	USAGE: python manip.py -r &lt;LINE NUMBER> &lt;FILE>  
	Example: python manip.py -r 36 test.py  

- Find/Replace (-f): replaces all occurences of the given word/phrase with the new word/phrase
	in the given file
	
	USAGE: python manip.py -f &lt;FIND> &lt;REPLACE> &lt;FILE>  
	Example: python manip.py -f hello world helloWorld.cpp  
	Example: python manip.py -f "variable = value" "variable=value" script.sh  
	
- Count (-c): outputs the number of occurences of the given string in the given file  

	USAGE: python manip.py -c &lt;STRING> &lt;FILE>  
	Example: python manip.py -c for program.cpp  
	Example: python manip.py -c "how many" words.txt
	
