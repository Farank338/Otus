import random
import time
import sys

import random
import time
import multiprocessing
import operator

sys. setrecursionlimit(10000000)

def CheckAlgorithm(func,func_name):
    for i in range(1,7,1):
        data=[random.random() for _ in range(pow(10,i))]
        start_time = time.time()

        p = multiprocessing.Process(target=func,args=(data,))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return

        func(data)
        print(func_name," sort ", pow(10,i) ," unsorted  in time\t",(time.time() - start_time))

        start_time = time.time()
        p = multiprocessing.Process(target=func,args=(data,))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        print(func_name," sort ", pow(10,i) ," sorted in time\t",(time.time() - start_time))

def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            (data[i], data[j]) = (data[j], data[i])
    (data[i + 1], data[high]) = (data[high], data[i + 1])
    return i + 1
 
 
def quickSort(data, low, high):    
    if low < high:
        pi = partition(data, low, high)
        quickSort(data, low, pi - 1)
        quickSort(data, pi + 1, high)

def QuickSort(data):    
    quickSort(data,0,len(data)-1)


def MergeSort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = MergeSort(L[:middle], compare)
        right = MergeSort(L[middle:], compare)
        return merge(left, right, compare)
    
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

CheckAlgorithm(QuickSort,"QuickSort")
CheckAlgorithm(MergeSort,"MergeSort")