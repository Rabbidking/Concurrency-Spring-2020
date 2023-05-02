#Garden turnstiles problem

import threading
import time

NUM_PEOPLE=10

def enter_gate():
    global count
    for i in range(NUM_PEOPLE):
        #<critical section>
        time.sleep(0)
        temp=count
        time.sleep(0)
        temp+=1
        time.sleep(0)
        count=temp
        time.sleep(0)
        #</critical section>
    print("All have entered.")
def exit_gate():
    global count
    for i in range(NUM_PEOPLE):
        #<critical section>
        time.sleep(0)
        temp=count
        time.sleep(0)
        temp-=1
        time.sleep(0)
        count=temp
        time.sleep(0)
        #</critical section>
    print("All have exited.")

while True:
    count=0
    print("Starting with",NUM_PEOPLE,"people.")
    t1=threading.Thread(target=enter_gate)
    t2=threading.Thread(target=exit_gate)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Finished with count of:",count)
    input("Press enter to continue.")
