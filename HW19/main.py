# Написать алгоритм поиска подстроки полным перебором, 2 байта.
def search_1(str,sub_str):
    if str==sub_str: return 0
    if len(sub_str)>=len(str): return -1

    pos=0
    while (1):
        if pos>=len(str):return -1          
        if len(str)-pos<len(sub_str):return -1
        if str[pos]!=sub_str[0]:
            pos=pos+1
            continue

        find=False
        for i in range(1,len(sub_str)):
            if i+pos>=len(str):break

            if str[pos+i]!=sub_str[i]:
                break

            if i==len(sub_str)-1:
                return pos

        pos=pos+1


# Оптимизировать алгоритм, используя сдвиги по префиксу шаблона, 2 байта.

def prefix(str):
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

def search_2(str, sub_str):
  sub_str_prefix = prefix(sub_str)
  i = 0 
  j = 0

  while (i < len(str)):
    if (str[i] == sub_str[j]):
        i=i+1
        j=j+1

        if j == len(sub_str):
            return i - len(sub_str)
      
    else:
      if j > 0:
        j = sub_str_prefix[j - 1]
      else:
        i=i+1

    if i == len(str) and j != (len(sub_str_prefix)):
        return -1



# Оптимизировать алгоритм, используя сдвиги по суффиксу текста, 2 байта.
def bisect_left(a, x, text, lo=0, hi=None):
    if lo < 0:
        return -1
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if text[a[mid]:]  == x:
            return a[mid]
        
        elif text[a[mid]:] < x: 
        	lo = mid+1
        else: 
            hi = mid
    if not text[a[lo]:].startswith(x): 
        return -1
    return a[lo]

def search_3(str, sub_str):
    text = str
    suffix = [text[i:] for i in range(len(text))]
    Sortedsuffix = sorted([text[i:] for i in range(len(text))])
    SuffixArray = [ suffix.index(ss) for ss in Sortedsuffix]
    return bisect_left(SuffixArray,sub_str,text)


# Реализовать алгоритм Бойера-Мура, 2 байта.

def badCharHeuristic(string, sub_str):
    badChar = [-1]*256
    for i in range(sub_str):
        badChar[ord(string[i])] = i;
    return badChar
 
def search_4(str, pat):
    m = len(pat)
    n = len(str)
    badChar = badCharHeuristic(pat, m) 
    s = 0
    while(s <= n-m):
        j = m-1
        while j>=0 and pat[j] == str[s+j]:
            j -= 1
 
        if j<0:
            return s
        else:
            s += max(1, j-badChar[ord(str[s+j])])
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





# Протестировать работу алгоритмов для разных начальных данных, 1 байт.
# Составить сравнительную таблицу по тестам и написать вывод, 1 байт.
# Для точного расчёта времени можно прогонять тест T раз и результат делить на T, где T = 10, 100, 1000 или ещё больше.

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

print('Написать алгоритм поиска подстроки полным перебором, 2 байта.')
test_algo(search_1)
print('Оптимизировать алгоритм, используя сдвиги по префиксу шаблона, 2 байта.')
test_algo(search_2)
print('Оптимизировать алгоритм, используя сдвиги по суффиксу текста, 2 байта.')
test_algo(search_3)
print('Реализовать алгоритм Бойера-Мура, 2 байта.')
test_algo(search_4)





