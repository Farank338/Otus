import splay 
import treap 
import random
import sys
import time
import multiprocessing
import numpy as np

sys.setrecursionlimit(10000000)



def Insert(tree,data,queue):
    for i in data:        
        tree.insert(i)
    queue.put(tree)
    

def Search(tree,data,queue):
    for i in data:
        if isinstance(tree,splay.SplayTree):
            tree.search_tree(i)
        else:
            tree.search(i)
    queue.put(tree)
    
def Delete(tree,data,queue):
    for i in data:
        if isinstance(tree,splay.SplayTree):
            tree.delete_node(i)
        else:
            tree.search(i)
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
        
        print(tree_name," insert ", len(data) ," in time\t\t",(time.time() - start_time))
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
        
        print(tree_name," search ", len(data) ," in time\t\t",(time.time() - start_time))
        t=queue.get()
        
        start_time = time.time()
        p = multiprocessing.Process(target=Delete, args=(t,data,queue))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        
        print(tree_name," delete ", len(data) ," in time\t\t",(time.time() - start_time))
        t=queue.get()
        
        
TestTree(splay.SplayTree,'SplayTree')
TestTree(treap.RandomizedBST,'RandomizedBST')



