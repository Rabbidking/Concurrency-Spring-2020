#John Bickel

import time
import random
import threading

s1 = threading.Semaphore(1)	#produces 1
s2 = threading.Semaphore(0)	#takes 1

def ME():
	for i in range(10):
		s1.acquire()
		print('M')
		pause()
		print('E')
		pause()
		s2.release()
		
def YOU():
	for i in range(10):
		s2.acquire()
		print('Y')
		pause()
		print('O')
		pause()
		print('U')
		pause()
		s1.release()

def pause():
	time.sleep(random.uniform(0.05, 0.1))
	
if __name__ == "__main__":
	
	t1 = threading.Thread(target = ME)
	t2 = threading.Thread(target = YOU)

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()