#John Bickel

import multiprocessing
import time
import os

def pi_est_even(num, even):
	total = 0
	for i in range(0, num, 2):
		if i % 2 == 0:
			total += 1 / (2 * i + 1)
	even.value = total
			
def pi_est_odd(num, odd):
	total = 0
	for i in range(0, num):
		if i % 2 > 0:
			total += -1 / (2 * i + 1)
	odd.value = total	

def pi_est_2proc(num):
	
	even_val = multiprocessing.Value('d')
	odd_val = multiprocessing.Value('d')

	process1 = multiprocessing.Process(target=pi_est_even, args=(1000000000, even_val,))
	process2 = multiprocessing.Process(target=pi_est_odd, args=(1000000000, odd_val,))
	
	#process1 = multiprocessing.Process(target=pi_est_even, args=(1000, even_val,))
	#process2 = multiprocessing.Process(target=pi_est_odd, args=(1000, odd_val,))
	
	process1.start()
	process2.start()

	process1.join()
	process2.join()
	
	print("Even value: " + str(even_val.value))
	print("Odd value: " + str(odd_val.value))
	
	total = even_val.value + odd_val.value
	print("Total: " + str(total))
	
	return total * 4
	

if __name__ == "__main__":
	
	t0 = time.time()
	print("Estimated value of pi: " + str(pi_est_2proc(1000000000)))
	#print("Estimated value of pi: " + str(pi_est_2proc(1000)))
	t1 = time.time()
	print("Execution time: " + str(t1 - t0))
	#input("Enter to exit")	