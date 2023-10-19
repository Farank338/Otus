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
        self.id=id
        self.degree_in=0
        self.degree_out=0

        pass

    def insert(self,connect):
        if connect in self.connection:
            return
        self.connection.append(connect)
        pass
    
    # считает степень вершины
    def calc_degree(self,con=None):
        if con is None:
            for i in self.connection:
                self.degree_out=self.degree_out+1
                if i is self:
                    self.degree_out=self.degree_out+1
                    continue
                i.calc_degree(self)
        else:
            self.degree_in=self.degree_in+1



class Graph:
    def __init__(self):
        self.nodes=[]

    def insert(self,vector):
        for i in range(0,len(vector)):
            self.nodes.append(GraphNode(i))
        
        for i in range(0,len(self.nodes)):
            for j in range(0,len(vector[i])):
                self.nodes[i].insert(self.nodes[vector[i][j]])

    def calc_degree(self,con=None):
        for i in self.nodes:
            i.calc_degree()

    def demucron_in(self):
        res=[]
        max=0
        for i in self.nodes:
            if i.degree_in>max:
                max=i.degree_in
        
        max=max+1
        for i in range(0,max):
            res.append([])
        
        for i in self.nodes:
            res[i.degree_in].append(i.id)
        return res
    
    def demucron_out(self):
        res=[]
        max=0
        for i in self.nodes:
            if i.degree_out>max:
                max=i.degree_out
        
        max=max+1
        for i in range(0,max):
            res.append([])
        
        for i in self.nodes:
            res[i.degree_out].append(i.id)
        return res
    
a=[
    [1,4],
    [2],
    [3],
    [1,4],
    [3],
]

b=Graph()
b.insert(a)
b.calc_degree()
print("Первый тест.png компоненты")
print("Результат алгоритма Демукрона по степеням входа",b.demucron_in())
print("Результат алгоритма Демукрона по степеням выхода",b.demucron_out())



print("Второй тест случайный граф")
# 5 вершин N, от 0 до 5 связей Smax в каждой
N, Smax = 5, 5
a=fill_vector(N,Smax)
for i in a:
    print(i)
b=Graph()
b.insert(a)
b.calc_degree()
print("Результат алгоритма Демукрона по степеням входа",b.demucron_in())
print("Результат алгоритма Демукрона по степеням выхода",b.demucron_out())

