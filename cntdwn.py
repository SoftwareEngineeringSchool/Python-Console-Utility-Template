#!/usr/bin/python
#look for right path in your system with command #which python

#this is simple template example of command line utility which will perform a countdown with little alarm
#cntdwn uses one required argument, -t to provide countdown time and one optional
#which is -b that stands for beep, producing a simple beep sound
#use it to grow your own project

import sys
# sys is system module for python which helps you to work with environement which your programm is running in

import time
# we need tiem module to be able to stop programm execution for a while (sleep function)

from termcolor import colored
#to be able to use this module you have to install it: #easy_install termcolor or $pip install termcolor

#let's get some staff from it
yourUtilityTitle 	= sys.argv[0]
arguments 			= sys.argv[1:]

#now it's time to perform something with our arguments

print colored("Hello dear user, you're running command line utility called " + yourUtilityTitle, "green")

#it's time to show up our arguments
for argument in arguments:
	print "argument " + str(arguments.index(argument)) + ": " + str(argument)

#let's define a variable to store timer count
count = 0

if '-t' in arguments:
	try:
		index = arguments.index('-t') + 1
		count = int(arguments[index])
	except:
		print colored("Something wrong happened to your time argument. Please provide it", "yellow")
else:
	print colored("Error: you didn't define time!", "red")

if count > 0:
	print colored("\nCountdown started:", "cyan")
	for i in xrange(int(count) + 1):
		time.sleep(1)
		print str(int(count) - i)

	if '-b' in arguments:
		print '\a'

#That's all folks ;)