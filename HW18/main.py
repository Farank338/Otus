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

class Link:
    def __init__(self,a,b,w):
        if a.id<b.id:
            self.a=a
            self.b=b
        else:
            self.b=a
            self.a=b
        self.weight=w
        
    def is_in(self,n):
        if self.a is n or self.b is n: return True
        else: return False

    def same(self,l):
        if self.a is l.a and self.b is l.b: return True
        else: return False

links=[]

def in_link(L):
    for j in links:
        if j.same(L):
            return True
    return False

class Node:
    def __init__(self,id:int=0):
        self.id:int=id
        self.connection=[]

    def add_connection(self,con):
        if con is self or con in self.connection:return;
        self.connection.append(con)
        con.add_connection(self)



    def add_link(self):
        for i in self.connection:                 
            L=Link(self,i,0)
            if in_link(L):continue
            links.append(L)

                    

   
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

nodes=[]
for k in range(0,len(a)):
    nodes.append(Node(k))

for k in range(0,len(a)):
    for k1 in range(0,len(a[k])):    
        nodes[k].add_connection(nodes[a[k][k1]])

for i1 in nodes:
    print("Узел ",i1.id," соединен с узлами ",end="")
    for i2 in i1.connection:
        print(i2.id,", ",end="")
    print()

for i in nodes:
    i.add_link()

w=1
for i in links:
    i.w=w
    w=w+1
exit(0)


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
w=1
for i in uniq_nodes_pair:
    nodes_pair__with_weight.append([i,w])
    w=w+1
    print(nodes_pair__with_weight[-1])

print("Результат алгоритма Дейкстры в виде массива из 2х чисел обозначающих вершины и число в виде суммы весов ребер по минимальному пути из ула А в Узел Б")

# Номер узла, массив связей с весами, и добавили посешена ли нода или нет
nodes_link_weight=[]
for i in range(0,len(a)):
    nodes_link_weight.append([i,[],None])

for i in nodes_link_weight:
    for j in nodes_pair__with_weight:
        if i[0]==j[0][0] or  i[0]==j[0][1]:
            i[1].append(j)


for a in nodes_link_weight:
    temp=nodes_link_weight.copy()
    print("Из узла А ", a[0]," в узел")
    
    a[2]=0
    # Проходим по узлам и вычисляем вес пути до соседних узлов
    for i in temp:
        index=temp.index(i)
        if i[0]==a[0]:continue

        for neigh in i[1]:
            if i[0]==neigh[0][0]:
                if temp[neigh[0][1]][2] is None or temp[neigh[0][1]][2]>neigh[1]:
                    temp[neigh[0][1]][2]=neigh[1]
            else:
                if temp[neigh[0][0]][2] is None or temp[neigh[0][0]][2]>neigh[1]:
                    temp[neigh[0][0]][2]=neigh[1]
                
                
    for i in temp:
        print(i)



# # 5 вершин N, от 0 до 5 связей Smax в каждой
# N, Smax = 5, 5
# a=fill_vector(N,Smax)
# for i in a:
#     print(i)

# print("Второй тест случайный граф")
# print("Поскольку в задании не сказано явно что граф взвешанный, но алгоритм Краскала применяется именно к взвешанному графу, уже отсортированный по весу связи")
# print("Распечатаем связи между узлами")
# nodes_pair=[]

# for i in range(0,len(a)):
#     for j in a[i]:
#         nodes_pair.append([i,j])

# for i in nodes_pair:
#     i.sort()

# uniq_nodes_pair=[]
# for i in nodes_pair:
#     if i not in uniq_nodes_pair:
#         uniq_nodes_pair.append(i)

# print(uniq_nodes_pair)

# print("Для задания веса просто пройдем по всем связям и расставим их вес с увеличением по счетчик, тогда будет следущий вектор смежности + вес связи, уже отсортированный по весу связи")
# nodes_pair__with_weight=[]
# w=0
# for i in uniq_nodes_pair:
#     nodes_pair__with_weight.append([i,w])
#     w=w+1
#     print(nodes_pair__with_weight[-1])

# print("Результат алгоритма Краскала в виде массива из 2х чисел обозначающих вершины")

# #  хранит узлы которые уже были пройдены
# c1=[]
# # хранит связи уже пройденные
# c2=[]
# for i in nodes_pair__with_weight:
#     link=i[0]  
#     if link[0] in c1 and link[1] in c1:
#         continue   
#     c1.extend(link)
#     c2.append(i)
#     print(link)

