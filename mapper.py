#!/usr/bin/python
#Python Hadoop Mapper

import sys

#input comes from STDIN (standard input)
for line in sys.stdin:
	line=line.strip()
	words=line.split()
	
	#following section will output each word with a count of 1
	#if a word appears twice, it will be output twice with a count 1
	#adding the counts is left upto the reducer
	for word in words:
		#write the results to STDOUT
		#this output will be input to reducer
		
		print '%s\t%s' % (word,1) 

