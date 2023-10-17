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

# Graph node
class GraphNode:
    def __init__(self,id):
        self.connection=[]
        self.connection_invert=[]
        self.id=id
        self.dfs_count:int=0
        self.dfs_flag:bool=False

        pass

    def insert(self,connect):
        if connect in self.connection:
            return
        self.connection.append(connect)
        pass

    def dfs_init(self):
        self.dfs_count:int=0
        self.dfs_flag:bool=False

    def dfs_run(self,cur:int=0):
        if self.dfs_flag is True:
            return
        self.dfs_flag=True
        self.dfs_count=cur
        for i in self.connection:
            if i.dfs_flag is True:
                continue
            r=i.dfs_run(self.dfs_count+1)
            self.dfs_count=r
        return self.dfs_count+1
    
    def insert_invert(self,connect):
        if connect in self.connection_invert:
            return
        self.connection_invert.append(connect)
        pass

    def invert(self):        
        for i in self.connection:
            i.insert_invert(self)
        return

    def kos(self,visited=[]):
        v=visited
        if self in v:
            return True,v
        v.append(self)
        for i in self.connection_invert:
            f,v=i.kos(v)
            if f is True:
                return f,v
            v=v[:v.index(self)+1]
            
        return False,v


class Graph:
    def __init__(self):
        self.nodes=[]

    def insert(self,vector):
        for i in range(0,len(vector)):
            self.nodes.append(GraphNode(i))
        
        for i in range(0,len(self.nodes)):
            for j in range(0,len(vector[i])):
                self.nodes[i].insert(self.nodes[vector[i][j]])

    def dfs(self):
        for i in self.nodes:
            i.dfs_init()
        for i in self.nodes:
            i.dfs_run(1)

    def invert(self):        
        for i in self.nodes:
            i.invert()
        return

    def kos(self):
        new_list = sorted(self.nodes, key=lambda x: x.dfs_count, reverse=True)
        
        used=[]
        res=[]
        for i in new_list:
            if i in used:
                continue
            l=[]
            f,v=i.kos(l)                

            r=[]
            for j in v:   
                r.append(j.id)      
                # print(j.id,end=' ')
                used.append(j)
            # print()
            res.append(r)
        return res







a=[
    [1,4],
    [2],
    [3],
    [1],
    [3],
]


b=Graph()
b.insert(a)
b.dfs()
b.invert()
print("Первый тест.png компоненты")
print("массива int[] component",b.kos())




print("Второй тест случайный граф")
# 5 вершин N, от 0 до 5 связей Smax в каждой
N, Smax = 5, 5
a=fill_vector(N,Smax)
for i in a:
    print(i)
b=Graph()
b.insert(a)
b.dfs()
b.invert()
print("массива int[] component",b.kos())
print("Второй тест случайны граф результаты")

