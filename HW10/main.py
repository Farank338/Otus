import  tree
import random
import sys
import time
import multiprocessing

sys.setrecursionlimit(10000000)

def InsertFunc(node,data):
    for i in data:
        node.insert(i,0)

def SearchFunc(node,data):
    for i in data:
        node.insert(i,0)
        node.has_key(i)
    
def RemoveFunc(node,data):
    for i in data:
        node.insert(i,0)
        node.remove(i)

def CheckAlgorithm(func_name,node):
    for i in range(1,7,1):
        power=pow(10,i)
        data=[ (int(random.random()*1000%1000)) for _ in range(power)]
        start_time = time.time()

        p = multiprocessing.Process(target=InsertFunc,args=(node,data))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
       
        print(func_name,pow(10,i) ,"insert in time\t\t",(time.time() - start_time))

        start_time = time.time()
        p = multiprocessing.Process(target=SearchFunc,args=(node,data))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return

        print(func_name,pow(10,i) ,"Search in time\t\t",(time.time() - start_time))

        start_time = time.time()
        p = multiprocessing.Process(target=RemoveFunc,args=(node,data))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return

        print(func_name,pow(10,i) ,"Remove in time\t\t",(time.time() - start_time))

        

tree_binary_sorted = tree.TreeBinary()
CheckAlgorithm("Binary tree",tree_binary_sorted)

avl_sorted = tree.TreeAVL()
CheckAlgorithm("AVL tree",avl_sorted)