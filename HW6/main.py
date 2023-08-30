import random
import time





def BubbleSort(data):
    buffer=0
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                buffer=data[j]
                data[j]=data[j+1]
                data[j+1]=buffer
    return data

def InsertionSort(data):
    buffer=0
    for i in range(1,len(data)):
        buffer=data[i]
        j=i-1
        while (j>=0 and data[j]>buffer):
            data[j+1]=data[j]
            j=j-1
        data[j+1]=buffer
    return data

def ShellSort(data):
    last_index = len(data)
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data


data_10000=[random.random() for _ in range(10000)]
data_1000=[random.random() for _ in range(1000)]
data_100=[random.random() for _ in range(100)]

print()

# BubbleSort
start_time = time.time()
BubbleSort(data_100)
print("BubbleSort sort 100 unsorted \t",(time.time() - start_time))

start_time = time.time()
BubbleSort(data_100)
print("BubbleSort sort 100 sorted\t",(time.time() - start_time))

start_time = time.time()
BubbleSort(data_1000)
print("BubbleSort sort 1000 unsorted\t",(time.time() - start_time))

start_time = time.time()
BubbleSort(data_1000)
print("BubbleSort sort 1000 sorted\t",(time.time() - start_time))

start_time = time.time()
BubbleSort(data_10000)
print("BubbleSort sort 10000 unsorted\t",(time.time() - start_time))

start_time = time.time()
BubbleSort(data_10000)
print("BubbleSort sort 10000 sorted\t",(time.time() - start_time))

# print(data_10000[:5],data_10000[-5:])
# print(data_1000[:5],data_1000[-5:])
# print(data_100[:5],data_100[-5:])

# InsertionSort
data_10000=[random.random() for _ in range(10000)]
data_1000=[random.random() for _ in range(1000)]
data_100=[random.random() for _ in range(100)]

start_time = time.time()
InsertionSort(data_100)
print("InsertionSort sort 100 unsorted\t",(time.time() - start_time))

start_time = time.time()
InsertionSort(data_100)
print("InsertionSort sort 100 sorted\t",(time.time() - start_time))

start_time = time.time()
InsertionSort(data_1000)
print("InsertionSort sort 1000 unsorted\t",(time.time() - start_time))

start_time = time.time()
InsertionSort(data_1000)
print("InsertionSort sort 1000 sorted\t",(time.time() - start_time))

start_time = time.time()
InsertionSort(data_10000)
print("InsertionSort sort 10000 unsorted\t",(time.time() - start_time))

start_time = time.time()
InsertionSort(data_10000)
print("InsertionSort sort 10000 sorted\t",(time.time() - start_time))

# ShellSort
data_10000=[random.random() for _ in range(10000)]
data_1000=[random.random() for _ in range(1000)]
data_100=[random.random() for _ in range(100)]

start_time = time.time()
ShellSort(data_100)
print("ShellSort sort 100 unsorted\t",(time.time() - start_time))

start_time = time.time()
ShellSort(data_100)
print("ShellSort sort 100 sorted\t",(time.time() - start_time))

start_time = time.time()
ShellSort(data_1000)
print("ShellSort sort 1000 unsorted\t",(time.time() - start_time))

start_time = time.time()
ShellSort(data_1000)
print("ShellSort sort 1000 sorted\t",(time.time() - start_time))

start_time = time.time()
ShellSort(data_10000)
print("ShellSort sort 10000 unsorted\t",(time.time() - start_time))

start_time = time.time()
ShellSort(data_10000)
print("ShellSort sort 10000 sorted\t",(time.time() - start_time))

# print(data_10000[:5],data_10000[-5:])
# print(data_1000[:5],data_1000[-5:])
# print(data_100[:5],data_100[-5:])

