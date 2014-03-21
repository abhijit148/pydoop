#!/usr/bin/python
#Python Reducer Script

from operator import itemgetter
import sys

current_word=None
current_count=0
word=None

#input from STDIN
for line in sys.stdin:
	line=line.strip()
	#parse the output of mapper.py i.e. input to reducer.py
	word,count=line.split('\t',1)
	
	#covert count (string) to int
	try:
		count=int(count)
	except ValueError:
		#Count was not a number. Ignore.
		continue
		
	#this IF-switch only works because Hadoop sorts map output
	#by key (here:word_ before it is passed to the reducer
	
	if current_word==word:
		current_count+=count
	else:
		if current_word:
			#write to STDOUT
			print '%s\t%s' % (current_word,current_count)
		
		current_count=count
		current_word=word
	
#For last word (if needed)
if current_word==word:
	print '%s\t%s' % (current_word,current_count)	
