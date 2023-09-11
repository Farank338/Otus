import random
import time
import sys

import random
import time
import multiprocessing
import operator

sys.setrecursionlimit(10000000)

def CountingSort(data):
    maxElement= max(data)
    countArrayLength = maxElement+1
    countArray = [0] * countArrayLength
    for el in data: 
        countArray[el] += 1
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 
    outputArray = [0] * len(data)
    i = len(data) - 1
    while i >= 0:
        currentEl = data[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    data=outputArray
    return data

def CountingSortRadix(data, exp1):
    n = len(data)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = data[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = data[i] // exp1
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(data)):
        data[i] = output[i]

def RadixSort(data):
    max1 = max(data)
    exp = 1
    while max1 / exp >= 1:
        CountingSortRadix(data, exp)
        exp *= 10
    return data
 
def insertion_sort(data):
    for i in range (1, len (data)):
        var = data[i]
        j = i - 1
        while (j >= 0 and var < data[j]):
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = var
 
def bucket_sort(data):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    max_value = max(data)
    size = max_value/len(data)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(data)):
        buckets_list.append([]) 

    # Put list elements into different buckets based on the size
    for i in range(len(data)):
        j = int (data[i] / size)
        if j != len (data):
            buckets_list[j].append(data[i])
        else:
            buckets_list[len(data) - 1].append(data[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(data)):
        insertion_sort(buckets_list[z])
            
    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len (data)):
        final_output = final_output + buckets_list[x]
    data=final_output
    return data

def CheckAlgorithm(func,func_name):
    for i in range(1,7,1):
        data=[ (int(random.random()*1000%1000)) for _ in range(pow(10,i))]
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
        print(func_name," sort ", pow(10,i) ," unsorted  in time\t\t",(time.time() - start_time))

        start_time = time.time()
        p = multiprocessing.Process(target=func,args=(data,))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        print(func_name," sort ", pow(10,i) ," sorted in time\t\t",(time.time() - start_time))


CheckAlgorithm(CountingSort,"CountingSort")
CheckAlgorithm(RadixSort,"RadixSort")
CheckAlgorithm(bucket_sort,"BucketSort")