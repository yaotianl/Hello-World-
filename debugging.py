"""Logging is a great way to understand what is happening in the program
	and in what order it is happening. When python logs an event, it creates
	a LogRecord object that holder information about that event.
	Don't debug with the print() function:
	It will end up spending a lot of time removing print() calls from the code
	for each log message. Might even remove nonlog print()
	While for logging, we can disable all easily.
""" 
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')
# Instead of displaying the log messages to the screen, write to a text file
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=
#'%(asctime)s- %(levelname)s- %(message)s')
#logging.disable(logging.CRITICAL)
# Logging levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.debug('Start of program')

def factorial(n):
	logging.debug('Start of factorial(%s)' % (n))
	total = 1
	for i in range(1, n+1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
	logging.debug('End of factorial(%s)' % (n))
	return total

print(factorial(5))
logging.debug('End of program')

