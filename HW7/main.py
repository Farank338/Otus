import random
import time
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000*100)



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

data_10000=[random.random() for _ in range(10000)]
data_1000=[random.random() for _ in range(1000)]
data_100=[random.random() for _ in range(100)]

print()

# SelectionSort
start_time = time.time()
SelectionSort(data_100)
print("SelectionSort sort 100 unsorted \t\t",(time.time() - start_time))

start_time = time.time()
SelectionSort(data_100)
print("SelectionSort sort 100 sorted\t\t",(time.time() - start_time))

start_time = time.time()
SelectionSort(data_1000)
print("SelectionSort sort 1000 unsorted\t\t",(time.time() - start_time))

start_time = time.time()
SelectionSort(data_1000)
print("SelectionSort sort 1000 sorted\t\t",(time.time() - start_time))

start_time = time.time()
SelectionSort(data_10000)
print("SelectionSort sort 10000 unsorted\t\t",(time.time() - start_time))

start_time = time.time()
SelectionSort(data_10000)
print("SelectionSort sort 10000 sorted\t\t",(time.time() - start_time))

# print(data_10000[:5],data_10000[-5:])
# print(data_1000[:5],data_1000[-5:])
# print(data_100[:5],data_100[-5:])

# HeapSort
data_10000=[random.random() for _ in range(10000)]
data_1000=[random.random() for _ in range(1000)]
data_100=[random.random() for _ in range(100)]

start_time = time.time()
HeapSort(data_100)
print("HeapSort sort 100 unsorted\t\t",(time.time() - start_time))

start_time = time.time()
HeapSort(data_100)
print("HeapSort sort 100 sorted\t\t",(time.time() - start_time))

start_time = time.time()
HeapSort(data_1000)
print("HeapSort sort 1000 unsorted\t\t",(time.time() - start_time))

start_time = time.time()
HeapSort(data_1000)
print("HeapSort sort 1000 sorted\t\t",(time.time() - start_time))

start_time = time.time()
HeapSort(data_10000)
print("HeapSort sort 10000 unsorted\t\t",(time.time() - start_time))

start_time = time.time()
HeapSort(data_10000)
print("HeapSort sort 10000 sorted\t\t",(time.time() - start_time))
