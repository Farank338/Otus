
#01. +1 байт. Реализовать итеративный O(N) алгоритм возведения числа в степень.
def power_iter(value,power):
    if power<0:return value
    if power==0:return 1    

    orig=value
    for i in range(power):
        value=value*orig
    return value
print('#01. +1 байт. Реализовать итеративный O(N) алгоритм возведения числа в степень.')
print(power_iter(2,0))
print(power_iter(2,1))
print(power_iter(2,2))
print(power_iter(2,3))

#02. +1 байт. Реализовать рекурсивный O(2^N) и итеративный O(N) алгоритмы поиска чисел Фибоначчи.
def fib_recursive(depth,prev1,prev2):
    if depth<=0:return prev1
    if depth==1:return prev2
    cur=prev1+prev2
    if depth==0: return cur
    else: return fib_recursive(depth-1,prev2,cur)

def fib_rec(depth):
    return fib_recursive(depth,0,1)

print('#02. +1 байт. Реализовать !рекурсивный O(2^N)! и итеративный O(N) алгоритмы поиска чисел Фибоначчи.')
print(fib_rec(0))
print(fib_rec(1))
print(fib_rec(2))
print(fib_rec(3))
print(fib_rec(4))
print(fib_rec(5))
print(fib_rec(6))
print(fib_rec(7))

def fib_iter(depth):
    if depth<=0:return 0
    if depth==1:return 1
    prev1=0
    prev2=1
    cur=0

    for i in range(depth-1):
        cur=prev1+prev2
        prev1=prev2
        prev2=cur

    return cur

print('#02. +1 байт. Реализовать рекурсивный O(2^N) и !итеративный O(N)! алгоритмы поиска чисел Фибоначчи.')
print(fib_iter(0))
print(fib_iter(1))
print(fib_iter(2))
print(fib_iter(3))
print(fib_iter(4))
print(fib_iter(5))
print(fib_iter(6))
print(fib_iter(7))

# 03. +1 байт. Реализовать алгоритм поиска количества простых чисел через перебор делителей, O(N^2).
def search_simple(simple_count):
    if simple_count==1:return 1,[2]
    if simple_count==2:return 2,[2,3]
    
    simple=[]
    number=2
    count=1
    while count!=simple_count:
        delit=0
        for i in range(number-2):           
            i=i+2
            
            if number%i==0:  
                delit=delit+1
                continue     
        if delit==0:       
            count=count+1
            simple.append(number) 
        number=number+1
    return count,simple

print(' 03. +1 байт. Реализовать алгоритм поиска количества простых чисел через перебор делителей, O(N^2).')

print(search_simple(1))
print(search_simple(2))
print(search_simple(3))
print(search_simple(4))
print(search_simple(10))