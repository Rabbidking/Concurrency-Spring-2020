import threading
import time

def dine():
	food = 100
	while food > 0:
		

n = int(input("Enter number of philsophers:"))
philosophers = []
for i in range(n):
	philsophers[i] = threading.Thread()