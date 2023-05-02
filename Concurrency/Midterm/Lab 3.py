import threading
import time
import random

#Two semaphores:
# items available to consume
# items available to produce
# produce one, wait, consume one, wait, repeat
s1 = threading.Semaphore(1)	#produces 1
s2 = threading.Semaphore(0)	#takes 1

buffer = 0

#s1.acquire()  #p() or wait()
#s1.release()  #v() or signal()

def producer():
	# This function will produce integers 1 through 100.
	# Each integer will be assigned, one at a time to a shared variable “buffer”.
	# After each number is produced, the program should sleep for between 0.001 and 0.01 seconds.
	# Once all numbers have been produced, print “Producer done.”
	
	global buffer

	for i in range(0, 100):
		s1.acquire()
		buffer = i + 1
		time.sleep(random.uniform(0.001, 0.01))
		s2.release()
		
	print("Producer done.")


def consumer():
	# This function will consume and print 100 values.
	# Each value will be retrieved by reading the shared variable “buffer”.
	# Print the number that was read.
	# After each number is printed, the program should sleep for between 0.001 and 0.01 seconds.
	# Once 100 numbers have been consumed, print “Consumer done.”
	
	global buffer

	for i in range(0, 100):
		s2.acquire()
		value = buffer
		print(value)
		time.sleep(random.uniform(0.001, 0.01))
		s1.release()

	print("Consumer done.")

t1 = threading.Thread(target = producer)
t2 = threading.Thread(target = consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done.")