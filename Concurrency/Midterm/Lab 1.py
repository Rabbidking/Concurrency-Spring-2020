import threading
import random
import time


class BankAccount(object):
    def __init__(self, initialBalance):
        self.balance = initialBalance
        self.transactionLog = []
        self.transactionLog.append("initial balance:" + str(initialBalance))

    def getBalance(self):
        time.sleep(random.uniform(0, 0.00001))
        temp = self.balance
        time.sleep(random.uniform(0, 0.00001))
        self.transactionLog.append("getBalance:" + str(temp))
        return temp

    def setBalance(self, amount):
        time.sleep(random.uniform(0, 0.00001))
        self.balance = amount
        time.sleep(random.uniform(0, 0.00001))
        self.transactionLog.append("setBalance:" + str(amount))

    def withdraw(self, amount):
        # This method withdraws funds by:
        # getting the balance using self.getBalance.
        # subtract the specified amount.
        # restore the amount using self.setBalance.
        # log the transaction as: "widthdraw("+str(amount)+")"
        curBal = self.getBalance()
        curBal = curBal - amount
        self.setBalance(curBal)
        self.transactionLog.append("widthdraw("+str(amount)+")")

    def deposit(self, amount):
        # This method deposits funds by:
        # getting the balance using self.getBalance.
        # adding the specified amount.
        # restore the amount using self.setBalance.
        # log the transaction as: "deposit("+str(amount)+")"
        curBal = self.getBalance()
        curBal = amount + curBal
        self.setBalance(curBal)
        self.transactionLog.append("deposit("+str(amount)+")")

# thread1 = threading.Thread(target = (reference to method or function), args = (tuple of arguments to pass to function/method))
# thread1 = threading.Thread(target = print, args = ("Hello",))
# thread1.start()
# ...do stuff... (two threads in use)
# thread1.join()	(joined back into one thread)

b = BankAccount(1000)
#b.deposit(500)
#b.withdraw(50)
#b.withdraw(10)
t1 = threading.Thread(target= b.deposit, args= (500,))
t2 = threading.Thread(target= b.withdraw, args= (50,))
t3 = threading.Thread(target= b.withdraw, args= (10,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(b.transactionLog)
print("Final balance: " + str(b.getBalance()))