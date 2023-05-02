import threading
import time

def philosopher(number):
	food = 100
	leftFork, rightFork = threading.Lock()
	
	while food > 0:
		print("P" + number + " is thinking...")
		time.sleep(random.uniform(0.2, 0.6))
		
		print("P" + number + " taking left fork...")
		leftFork.acquire()	#pick up left fork
		time.sleep(0.01)		#pause for 0.01 seconds
		
		print("P" + number + " taking right fork...")
		rightFork.acquire()	#pick up right fork
		time.sleep(0.01)		#pause for 0.01 seconds
		
		print("P" + number + " is eating...")	#eat food
		food -= random.uniform(5, 10)
		print("P" + number + " is pausing with " + self.food + " left")
		time.sleep(random.uniform(0.2, 0.6))		#pause
	
	print("P" + self.number + " is done!")
	self.rightFork.release()	#drop right fork
	self.leftFork.release()		#drop left fork	

n = int(input("Enter number of philsophers:"))


for i in range(n):
	thread = threading.Thread(target = philosopher, args=(i))
	thread.start()

	
print("Everyone is done!")