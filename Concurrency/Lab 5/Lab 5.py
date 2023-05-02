import urllib.request
import threading
import time
import os

sequentialTime = 0
concurrentTime = 0
threads = []

def fileDownload(url, filename):
	start = time.time()
	urllib.request.urlretrieve("http://" + url, filename)
	stop = time.time()
	img_time = stop - start
	print("Time to download " + str(filename) + ": " + str(img_time))

def downloadSequential(filesToDownloadList):
	global sequentialTime
	print("SEQUENTIAL DOWNLOAD:")
	time0 = time.time()
	for i in range(len(filesToDownloadList)):
	
		url_of_file = filesToDownloadList[i]
		parts = url_of_file.split('/')
		output_file_name = parts[-1]
		
		fileDownload(url_of_file, output_file_name)
		
	time1 = time.time()
	sequentialTime = time1 - time0
	print("Total time: " + str(sequentialTime) + '\n')
	
def downloadConcurrent(filesToDownloadList):
	global concurrentTime
	print("CONCURRENT DOWNLOAD:")
	time0 = time.time()
	
	for url in filesToDownloadList:
		parts = url.split('/')
		filename = parts[-1]
		
		t = threading.Thread(target = fileDownload, args = (url, filename))
		threads.append(t)
		
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()	
	
	time1 = time.time()
	concurrentTime = time1 - time0
	print("Total time: " + str(concurrentTime) + '\n')

fileList=["images-assets.nasa.gov/image/PIA04921/PIA04921~orig.jpg",
		"images-assets.nasa.gov/image/PIA10600/PIA10600~orig.jpg",
		"images-assets.nasa.gov/image/GSFC_20171208_Archive_e001925/GSFC_20171208_Archive_e001925~orig.jpg",
		"images-assets.nasa.gov/image/PIA11999/PIA11999~orig.jpg",
		"images-assets.nasa.gov/image/GSFC_20171208_Archive_e001262/GSFC_20171208_Archive_e001262~orig.jpg",
		"images-assets.nasa.gov/image/PIA15536/PIA15536~orig.jpg",
		"images-assets.nasa.gov/image/PIA00583/PIA00583~orig.jpg",
		"images-assets.nasa.gov/image/GSFC_20171208_Archive_e001762/GSFC_20171208_Archive_e001762~orig.jpg",
		"images-assets.nasa.gov/image/PIA05185/PIA05185~orig.jpg",
		"images-assets.nasa.gov/image/PIA03225/PIA03225~orig.jpg"]		

downloadSequential(fileList)
downloadConcurrent(fileList)
	
print("Total sequential speedup: ", sequentialTime)
print("Total concurrent speedup: ", concurrentTime)
speedup = sequentialTime / concurrentTime

if(sequentialTime < concurrentTime):
	print("Sequential was faster.")
else:
	print("Concurrent was faster.")
print("Speedup of ", speedup)

