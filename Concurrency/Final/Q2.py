#John Bickel

import time
import random
import threading

lock = threading.Lock()

def ME():
	for i in range(10):
		lock.acquire()
		print('M')
		pause()
		print('E')
		pause()
		lock.release()
		
def YOU():
	for i in range(10):
		lock.acquire()
		print('Y')
		pause()
		print('O')
		pause()
		print('U')
		pause()
		lock.release()

def pause():
	time.sleep(random.uniform(0.05, 0.1))
	
if __name__ == "__main__":
	
	t1 = threading.Thread(target= ME)
	t2 = threading.Thread(target= YOU)

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()