from tree import *
import random
import sys
import time
import multiprocessing
import numpy as np

sys.setrecursionlimit(10000000)

def Insert(tree,data,queue):
    for i in data:
        tree.insert(i,0)
    queue.put(tree)
    

def Search(tree,data,queue):
    for i in data:
        tree.get_value(i)
    queue.put(tree)
    
def Delete(tree,data,queue):
    for i in data:
        tree.remove(i)
    queue.put(tree)

def TestTree(constructor,tree_name):
    t=constructor()
    for i in range(1,7,1):
        power=pow(10,i)
        queue = multiprocessing.Queue()
        data = np.random.randint(0,1000,power)
        start_time = time.time()

        p = multiprocessing.Process(target=Insert, args=(t,data,queue))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        
        print(tree_name," insert ", power ," in time\t\t",(time.time() - start_time))
        t=queue.get()

        data = data[:int(power/10)]
        start_time = time.time()
        p = multiprocessing.Process(target=Search, args=(t,data,queue))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        
        print(tree_name," search ", power ," in time\t\t",(time.time() - start_time))
        t=queue.get()
        
        start_time = time.time()
        p = multiprocessing.Process(target=Search, args=(t,data,queue))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        
        print(tree_name," delete ", power ," in time\t\t",(time.time() - start_time))
        t=queue.get()
        
        
TestTree(TreeBinary,'Binary')
TestTree(TreeAVL,'AVL')

# t=TreeAVL()
# for i in t:
#     print(i)

# data = np.random.randint(1,101,5)

# data=[0,-2,2,-1,-3,1,3]
# for i in data:
#     t.insert(i,0)
#     print(i,end=' ')
# print() 

# for i in t:
#     print(i,end=' ')
# print()

# for i in data:
#     print(t.get_value(i),i)
# print()

# for i in t:
#     print(i,end=' ')
# print()

# for i in data:
#     print(t.remove(i),i)
# print()
