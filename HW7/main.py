import random
import time
import sys

import random
import time
import multiprocessing



def CheckAlgorithm(func,func_name):
    for i in range(1,10,1):
        data=[random.random() for _ in range(pow(10,i))]
        start_time = time.time()

        p = multiprocessing.Process(target=func,args=(data,))
        p.start()
        p.join(10)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return

        func(data)
        print(func_name," sort ", pow(10,i) ," unsorted \t",(time.time() - start_time))

        start_time = time.time()
        p = multiprocessing.Process(target=func,args=(data,))
        p.start()
        p.join(10)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        print(func_name," sort ", pow(10,i) ," sorted\t",(time.time() - start_time))

def SelectionSort(data):
    for i in range(len(data) - 1):
        min_index = i
        for k in range(i + 1, len(data)):
            if data[k] < data[min_index]:
                min_index = k
        data[i], data[min_index] = data[min_index], data[i]
    return data

def heapify(data, n, i):
    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2   
    if l < n and data[i] < data[l]:
        largest = l 
    if r < n and data[largest] < data[r]:
        largest = r
    if largest != i:
        (data[i], data[largest]) = (data[largest], data[i])
        heapify(data, n, largest)
 
def HeapSort(data):
    n = len(data) 
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i) 

    for i in range(n - 1, 0, -1):
        (data[i], data[0]) = (data[0], data[i])  # swap
        heapify(data, i, 0)
    return data

CheckAlgorithm(SelectionSort,"SelectionSort")
CheckAlgorithm(HeapSort,"HeapSort")
