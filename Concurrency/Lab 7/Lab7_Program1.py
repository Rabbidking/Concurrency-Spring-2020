#John Bickel

import time

def pi_est_sequential(num):
	total = 0
	for i in range(0, num):
		total += (-1) ** i / (2 * i + 1)
	return total * 4

if __name__ == "__main__":
	t0 = time.time()
	print("Estimated value of pi: " + str(pi_est_sequential(1000000000)))
	t1 = time.time()
	print("Execution time: " + str(t1 - t0))