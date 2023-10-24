from random import randrange




def fill_vector(size, link_number):
    v=[]
    #поскольку по заданию 0 это валидный номер вершины то массив будет инициализирован без 0  
    for i in range(0,size):
        v.append([])
        for j in range(0,randrange(link_number)):
            r=randrange(size)
            if r in v[i]:
                continue
            v[i].append(r)
    return v

   
a=[
    [1,4],
    [2],
    [3],
    [1,4],
    [3],
]

print("Первый тест.png компоненты")
print("Поскольку в задании не сказано явно что граф взвешанный, но алгоритм Краскала применяется именно к взвешанному графу")
print("Распечатаем связи между узлами")
nodes_pair=[]

for i in range(0,len(a)):
    for j in a[i]:
        nodes_pair.append([i,j])

for i in nodes_pair:
    i.sort()

uniq_nodes_pair=[]
for i in nodes_pair:
    if i not in uniq_nodes_pair:
        uniq_nodes_pair.append(i)

print(uniq_nodes_pair)

print("Для задания веса просто пройдем по всем связям и расставим их вес с увеличением по счетчик, тогда будет следущий вектор смежности + вес связи")
nodes_pair__with_weight=[]
w=0
for i in uniq_nodes_pair:
    nodes_pair__with_weight.append([i,w])
    w=w+1
    print(nodes_pair__with_weight[-1])

print("Результат алгоритма Краскала в виде массива из 2х чисел обозначающих вершиных")

#  хранит узлы которые уже были пройдены
c1=[]
# хранит связи уже пройденные
c2=[]
for i in nodes_pair__with_weight:
    link=i[0]  
    if link[0] in c1 and link[1] in c1:
        continue   
    c1.extend(link)
    c2.append(i)
    print(link)




# 5 вершин N, от 0 до 5 связей Smax в каждой
N, Smax = 5, 5
a=fill_vector(N,Smax)
for i in a:
    print(i)

print("Второй тест случайный граф")
print("Поскольку в задании не сказано явно что граф взвешанный, но алгоритм Краскала применяется именно к взвешанному графу")
print("Распечатаем связи между узлами")
nodes_pair=[]

for i in range(0,len(a)):
    for j in a[i]:
        nodes_pair.append([i,j])

for i in nodes_pair:
    i.sort()

uniq_nodes_pair=[]
for i in nodes_pair:
    if i not in uniq_nodes_pair:
        uniq_nodes_pair.append(i)

print(uniq_nodes_pair)

print("Для задания веса просто пройдем по всем связям и расставим их вес с увеличением по счетчик, тогда будет следущий вектор смежности + вес связи")
nodes_pair__with_weight=[]
w=0
for i in uniq_nodes_pair:
    nodes_pair__with_weight.append([i,w])
    w=w+1
    print(nodes_pair__with_weight[-1])

print("Результат алгоритма Краскала в виде массива из 2х чисел обозначающих вершиных")

#  хранит узлы которые уже были пройдены
c1=[]
# хранит связи уже пройденные
c2=[]
for i in nodes_pair__with_weight:
    link=i[0]  
    if link[0] in c1 and link[1] in c1:
        continue   
    c1.extend(link)
    c2.append(i)
    print(link)

