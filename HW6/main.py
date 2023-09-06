import random
import time
import multiprocessing

def CheckAlgorithm(func,func_name):
    for i in range(1,5,1):
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
        print(func_name," sort ", pow(10,i) ," unsorted \t",(time.time() - start_time))

        start_time = time.time()
        p = multiprocessing.Process(target=func,args=(data,))
        p.start()
        p.join(120)
        if p.is_alive():
            p.terminate()
            p.kill()
            p.join()
            return
        print(func_name," sort ", pow(10,i) ," sorted\t",(time.time() - start_time))


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

CheckAlgorithm(BubbleSort,"BubbleSort")
CheckAlgorithm(InsertionSort,"InsertionSort")
CheckAlgorithm(ShellSort,"ShellSort")
exit(0)

