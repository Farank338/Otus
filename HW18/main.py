class Link:
    def __init__(self,a,b,w):
        if a.id<b.id:            
            self.a=a
            self.b=b
        else:
            self.b=a
            self.a=b
        self.w=w
        
    def is_in(self,n):
        if self.a is n or self.b is n: return True
        else: return False

    def not_me(self,a_or_b):
        if a_or_b is not self.a and a_or_b is not self.b:return None
        if a_or_b is self.a: return self.b
        return self.a

def link_in_links(links,link):
    for i in links:
        if i.is_in(link) is True:return True
    return False

class Node:
    def __init__(self,id:int=0):
        self.id:int=id
        self.links=[]
        self.weight=None
        self.visited=False

            
    def add_link(self,l:Link):
        if link_in_links(self.links,l) is False:
            self.links.append(l)

    def visit(self):
        self.visited=True
        for i in self.links:
            neigh=i.not_me(self)
            my_weight=self.weight+i.w
            if neigh.weight is None:
                neigh.weight=my_weight
                continue
            if neigh.weight>my_weight:
                neigh.weight=my_weight


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

def create_graph(vector):
    nodes=[]
    for k in range(0,len(vector)):
        nodes.append(Node(k))

    w=1
    for k in range(0,len(vector)):
        for i in vector[k]:
            if nodes[k] is nodes[i]: continue
            l=Link(nodes[k],nodes[i],w)
            nodes[k].add_link(l)
            nodes[i].add_link(l)
            w=w+1
    return nodes

def find_lowest_unvisited(nodes):
    min=None
    for i in nodes:
        if i.weight is None:
            continue
        if min is None and i.visited is False: 
            min=i
            continue
        if min is None:
            continue
        if min.weight<i.weight and i.visited is False:
            min=i
            continue
    return min

def dekstra(vector):
    for node_1 in range(0,len(vector)):      
        nodes=create_graph(vector)
        nodes[node_1].weight=0
        lowest=find_lowest_unvisited(nodes)
        while (lowest is not None):
            lowest.visit()
            lowest=find_lowest_unvisited(nodes)

        print('Из узла',node_1,'до узла')
        for i in nodes:  
            if i.id == node_1:continue
            print('\t',i.id,'минимальный путь составит',i.weight)
            
    

   
a=[
    [1,4],
    [2],
    [3],
    [1,4],
    [3],
]


print("Первый тест.png компоненты")
for i in a:
    print(i)
print("Прочитаем вектр смежности, с генерируем веса связей и распечатаем")
nodes=create_graph(a)

for i in nodes:
    print(i.id)
    for l in i.links:
        print('\tw',l.w,'node a',l.a.id,'node b,',l.b.id)
dekstra(a)

print("Второй тест случайный граф")
# 5 вершин N, от 0 до 5 связей Smax в каждой
N, Smax = 5, 5
a=fill_vector(N,Smax)
for i in a:
    print(i)


print("Прочитаем вектр смежности, с генерируем веса связей и распечатаем")
nodes=create_graph(a)

for i in nodes:
    print(i.id)
    for l in i.links:
        print('\tw',l.w,'node a',l.a.id,'node b,',l.b.id)
dekstra(a)