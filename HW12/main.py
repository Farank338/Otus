import chain
import pirson
import sys

import random
import sys
import time
import multiprocessing
import numpy as np

sys.setrecursionlimit(30000)

def insert(hash_table,data,queue):
    for i in data:        
        hash_table.insert(i)
    queue.put(hash_table)
    

def find(hash_table,data,queue):
    for i in data:        
        hash_table.find(i)
    queue.put(hash_table)
    
def remove(hash_table,data,queue):
    for i in data:   
        hash_table.remove(i)
    queue.put(hash_table)

def Test(HashTable,name):
    t=HashTable()
    to_sleep=120
    for i in range(1,7,1):
        power=pow(10,i)
        queue = multiprocessing.Queue()
        data = np.random.randint(0,1000,power)
        start_time = time.time()

        p = multiprocessing.Process(target=insert, args=(t,data,queue))
        p.start()
        p.join(to_sleep)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        
        print(name," insert ", len(data) ," in time\t\t",(time.time() - start_time))
        t=queue.get()

        data = data[:int(power/10)]
        start_time = time.time()
        p = multiprocessing.Process(target=find, args=(t,data,queue))
        p.start()
        p.join(to_sleep)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        
        print(name," search ", len(data) ," in time\t\t",(time.time() - start_time))
        t=queue.get()
        
        start_time = time.time()
        p = multiprocessing.Process(target=remove, args=(t,data,queue))
        p.start()
        p.join(to_sleep)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        
        print(name," delete ", len(data) ," in time\t\t",(time.time() - start_time))
        t=queue.get()

Test(chain.HashTable,'chain.HashTable')
Test(pirson.HashTable,'pirson.HashTable')

