
from threading import Thread
import threading
import time
from multiprocessing import Process, Lock
import multiprocessing

threadLock = threading.Lock()
processLock = multiprocessing.Lock()
processLockx = multiprocessing.Lock()

def carre(tab):
    i = 0
    while (i < len(tab)):
        print ("carre de tab[",i,"] = ",tab[i] , " ==> ", pow(tab[i],2))
        time.sleep(0.51)
        i += 1


def cub(tab):
    i = 0
    while (i < len(tab)):
        print ("cub de tab[",i,"] = ",tab[i] , " ==> ", pow(tab[i],3))
        time.sleep(0.51)
        i += 1


class myThread (threading.Thread):
    def __init__(self, threadID, name, fct, args):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.args = args
        self.fct = fct

    def run(self):
      # Get lock to synchronize threads
        threadLock.acquire()
        print("\n------------------------Thread Simulation ",self.threadID, " -----------------------------------")
        self.fct(self.args)
        # Free lock to release next thread
        threadLock.release()


class Worker(Process):
    def __init__(self, processID, name, fct, args):
        Process.__init__(self)
        self.processID = processID
        self.name = name
        self.args = args
        self.fct = fct
    
    def run(self):
        processLock.acquire()
        print("\n------------------------Process Simulation ",self.processID, " -----------------------------------")
        self.fct(self.args)
        processLock.release()

def multithreading_simulation():
    
    th = myThread(1, "Thread-carre", carre, [5,6,7,8,9,7,55])
    thx = myThread(2, "Thread-cub", cub, [5,6,7,8,9,7,55])
    th.start()
    thx.start()

    th.join()
    thx.join()
    
    
def multiprocessing_simulation():
    worker = Worker(1, "process-carre", carre, [5,6,7])
    worker.start()

    worker2 = Worker(2, "process-cub", cub, [5,6,7])
    worker2.start()

    worker.join()
    worker2.join()

if __name__ == '__main__':
    multithreading_simulation()
    multiprocessing_simulation()