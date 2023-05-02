import threading
import time
import random

def Fab1():
	for i in range(1, 11, 2):
		cv4 = threading.Condition()
		cv4.acquire()
		print("Fab1 produced Car"+str(i))
		paint.Place(i)
		print("Fab1 sent Car" + str(i) + " to painting queue")
		cv4.notifyAll()
		cv4.release()

def Fab2():
	for j in range(2, 11, 2):
		cv3 = threading.Condition()
		cv3.acquire()
		print("Fab2 produced Car"+str(j))
		paint.Place(j)
		print("Fab2 sent Car" + str(j) + " to painting queue")
		cv3.notifyAll()
		cv3.release()

class paint_class():

	def __init__(self):
		self.paint_buffer_array = []
		self.item_count = 0
		self.cv = threading.Condition()

	def Place(self, value):
	
		self.cv.acquire()
		time.sleep(random.uniform(0.001, 0.01))
		
		while self.item_count >= 4:
			if value in range(1, 11, 2):
				print("Fab1 stopped - painting queue full.")
			else:
				print("Fab2 stopped - painting queue full.")
			self.cv.wait()
			
		print("Painting queue received Car" + str(value))
		self.paint_buffer_array.append(value)
		self.item_count = self.item_count + 1
		self.cv.notifyAll()
		time.sleep(random.uniform(0.001, 0.01))
		self.cv.release()

	def Take(self, value):
	
		self.cv.acquire()
		time.sleep(random.uniform(0.001, 0.01))
		
		while self.item_count == 0:
			#print(value + " stopped - painting queue empty")
			self.cv.wait()
			
		value = self.paint_buffer_array.pop(0)
		self.item_count = self.item_count - 1
		self.cv.notifyAll()
		time.sleep(random.uniform(0.001, 0.01))
		self.cv.release()
		return value

	#cv.acquire() or cv.release() OR with cv: (loop)
	#cv.wait() ---> release lock and awaken (want a while loop around it)	(while buffer is full: cv.wait())
	#cv.notify() OR cv.notifyAll() ---> notifyAll recommended!

class finish_class():

	def __init__(self):
		self.finish_buffer_array = []
		self.item_count = 0
		self.cv2 = threading.Condition()

	def Place(self, value):
	
		self.cv2.acquire()
		time.sleep(random.uniform(0.001, 0.01))
		
		while self.item_count >= 4:
			if value in range(1, 11, 2):
				print("Fab1 stopped - finishing queue full.")
			else:
				print("Fab2 stopped - finishing queue full.")
			self.cv2.wait()
			
		print("Finishing queue received Car" + str(value))
		self.finish_buffer_array.append(value)
		self.item_count = self.item_count + 1
		self.cv2.notifyAll()
		time.sleep(random.uniform(0.001, 0.01))
		self.cv2.release()

	def Take(self, value):
	
		self.cv2.acquire()
		time.sleep(random.uniform(0.001, 0.01))
		
		while self.item_count == 0:
			#print(value + " stopped - finishing queue empty")
			self.cv2.wait()
			
		value = self.finish_buffer_array.pop(0)
		self.item_count = self.item_count - 1
		self.cv2.notifyAll()
		time.sleep(random.uniform(0.001, 0.01))
		self.cv2.release()
		return value

def paint_to_finish():
	for i in range(1, 11):
		paint.Take(i)
		finish.Place(i)
		print("Painting sent Car" + str(i) + " to Finishing")

def completed_cars():
	for i in range(1, 11):
		finish.Take(i)
		print("Finishing sent Car" + str(i) + " to Completed")
		completed_array.append(i)

paint = paint_class()
finish = finish_class()
completed_array = [] 

fab1 = threading.Thread(target = Fab1)
fab2 = threading.Thread(target = Fab2)
paint_to_finish = threading.Thread(target = paint_to_finish)
completed_cars = threading.Thread(target = completed_cars)

fab1.start()
fab2.start()
paint_to_finish.start()
completed_cars.start()

fab1.join()
fab2.join()
paint_to_finish.join()
completed_cars.join()

#car_1 is a string
#put some time.sleeps inside the loops
