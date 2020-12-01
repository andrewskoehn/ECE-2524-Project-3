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

- Comment (-t): comments the given lines in the given file; the line range is inclusive; user must
	provide the appropriate commenting character for the given file type/language  
	
	USAGE: python manip.py -t &lt;COMMENT> &lt;START> &lt;END> &lt;FILE>  
	Example: python manip.py -t // 1 3 helloWorld.cpp  
	Example: python manip.py -t "#" 5 5 test.py  
	
	Note: this operation does not check for the correct commenting character, so it can also be used
	to insert any kind of character/string at the beginning of the given lines

The program implements usage error checking and handling. It also implements
file error checking and handling. When an error occurs, an appropriate message is displayed
to the user. Also, when certain situations occur, an appropriate message is displayed
to the user (i.e., if no occurences of a string are found in -f or -c or a given line does not
exist in -r or -t).  

Note: the program cannot execute multiple operations in one call. In other words, each
call to manip.py must flag and execute only one of the available operations.  

EXAMPLES

If "text.txt" contains:  
>>this is a text file  
with two lines  
	
then executing  
	>>python manip.py -a "append" text.txt  
will result in "text.txt" containing:  
>>this is a text file  
with two linesappend

and then executing  
	>>python manip.py -r 2 text.txt  
will result in "text.txt" containing:
>>this is a text file

and then executing  
	>>python manip.py -f "text file" "textfile" text.txt  
will result in "text.txt" containing:
>>this is a textfile
	
and then executing  
	>>python manip.py -c i text.txt  
will output  
>>3 occurence(s) of "i" found.
	
and then executing  
	>>python manip.py -t # 2 5 text.txt  
will output  
>>File does not contain the given line range.
