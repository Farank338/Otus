# Составить конечный автомат и прохождение по нему для поиска шаблона в строке, 2 байта.
NO_OF_CHARS = 256
 
def getNextState(pat, M, state, x):
    if state < M and x == ord(pat[state]):
        return state+1
 
    i=0
    for ns in range(state,0,-1):
        if ord(pat[ns-1]) == x:
            while(i<ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i+=1
            if i == ns-1:
                return ns 
    return 0
 
def computeTF(pat, M):
    global NO_OF_CHARS
 
    TF = [[0 for i in range(NO_OF_CHARS)]\
          for _ in range(M+1)]
 
    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z
 
    return TF
 
def search_1(pat, txt):
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)    
    state=0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            print("Pattern found at index: {}".\
                   format(i-M+1))
            return i-M+1
    return -1

# Самостоятельно написать функцию вычисления префикс-функции, медленный вариант, 2 байта.



def prefix_function(str):
    n = len(str)
    pi=[0]*n
    for i in range(1,n):
        j = pi[i-1]
        while (j > 0 and str[i] != str[j]):
            j = pi[j-1]
        if (str[i] == str[j]):
            j=j+1
        pi[i] = j    
    return pi

# Переписать алгоритм быстрого вычисления префикс-функции и разобраться в нём, 2 байта.

def prefix_function_fast(str):
    n = len(str)
    p = [0]*n
    i = 1
    j = 0
    while (i < n):
        if (str[i] == str[j]):
            p[i] = j + 1
            i=i+1
            j=j+1
        else:
            if j == 0:
                p[i] = 0
                i=i+1
            else:
                j = p[j - 1]

    return p



# Реализовать алгоритм Кнута-Морриса-Пратта, 2 байта.
def KMP(text,pattern):
    maxShift = prefix_function(pattern)
    p = 0
    t = 0
    while t < len(text):
        if(pattern[p] == text[t]):
            p +=1
            t +=1
            if(p >= len(pattern)):
                return t-p
        elif p != 0:
            p = maxShift[p-1]
        else:
            t +=1
    return -1

def KMP_fast(text,pattern):
    maxShift = prefix_function_fast(pattern)
    p = 0
    t = 0
    while t < len(text):
        if(pattern[p] == text[t]):
            p +=1
            t +=1
            if(p >= len(pattern)):
                return t-p
        elif p != 0:
            p = maxShift[p-1]
        else:
            t +=1
    return -1

import random
import time
import sys
import string

import random
import time
import multiprocessing

def run_algo(algo,text,word):    
    algo(text,word)



def test_algo(algo):
    
    start_time = time.time()
    cycle=10
    while cycle<=10000000000000:
        text=''.join(random.choices(string.ascii_uppercase + string.digits, k=cycle))
        to_search=''.join(random.choices(string.ascii_uppercase + string.digits, k=int(cycle/10)))
        p = multiprocessing.Process(target=run_algo,args=(algo,text,to_search))
        p.start()
        p.join(30)
        if p.is_alive():
            p.terminate();p.kill();p.join();return        

        print("\t sub srting search ", cycle ," in time\t\t\t",(time.time() - start_time))
        
        cycle=cycle*10

print('Составить конечный автомат и прохождение по нему для поиска шаблона в строке, 2 байта.')
test_algo(search_1)

print('Реализовать алгоритм Кнута-Морриса-Пратта, 2 байта.')
print('Самостоятельно написать функцию вычисления префикс-функции, медленный вариант, 2 байта.')
print('Кнута-Морриса-Пратта + префикс-функции, медленный вариант')
test_algo(KMP)

print('Переписать алгоритм быстрого вычисления префикс-функции и разобраться в нём, 2 байта.')
print('Кнута-Морриса-Пратта + алгоритм быстрого вычисления префикс-функции')
test_algo(KMP_fast)
