#John Bickel

import multiprocessing
import time
import os

def pi_est_1(num, first):
	total = 1
	for i in range(1, num, 8):
		total += 1 / i
	first.value = total
			
def pi_est_2(num, second):
	total = -1
	for i in range(3, num, 8):
		total += -1 / i
	second.value = total	
	
def pi_est_3(num, third):
	total = 1
	for i in range(5, num, 8):
		total += 1 / i
	third.value = total
	
def pi_est_4(num, fourth):
	total = -1
	for i in range(7, num, 8):
		total += -1 / i
	fourth.value = total

def pi_est_4proc(num):
	
	first_val = multiprocessing.Value('d')
	second_val = multiprocessing.Value('d')
	third_val = multiprocessing.Value('d')
	fourth_val = multiprocessing.Value('d')

	process1 = multiprocessing.Process(target=pi_est_1, args=(1000000000, first_val,))
	process2 = multiprocessing.Process(target=pi_est_2, args=(1000000000, second_val,))
	process3 = multiprocessing.Process(target=pi_est_3, args=(1000000000, third_val,))
	process4 = multiprocessing.Process(target=pi_est_4, args=(1000000000, fourth_val,))
	
	#process1 = multiprocessing.Process(target=pi_est_1, args=(1000, first_val,))
	#process2 = multiprocessing.Process(target=pi_est_2, args=(1000, second_val,))
	#process3 = multiprocessing.Process(target=pi_est_3, args=(1000, third_val,))
	#process4 = multiprocessing.Process(target=pi_est_4, args=(1000, fourth_val,))
	
	
	process1.start()
	process2.start()
	process3.start()
	process4.start()

	process1.join()
	process2.join()
	process3.join()
	process4.join()
	
	print("Process 1 value: " + str(first_val.value))
	print("Process 2 value: " + str(second_val.value))
	print("Process 3 value: " + str(third_val.value))
	print("Process 4 value: " + str(fourth_val.value))
	
	total = first_val.value + second_val.value + third_val.value + fourth_val.value
	print("Total: " + str(total))
	
	return total * 4
	

if __name__ == "__main__":
	
	t0 = time.time()
	print("Estimated value of pi: " + str(pi_est_4proc(1000000000)))
	#print("Estimated value of pi: " + str(pi_est_4proc(1000)))
	t1 = time.time()
	print("Execution time: " + str(t1 - t0))
	#input("Enter to exit")	