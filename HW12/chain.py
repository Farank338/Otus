class List:
    def __init__(self,data:int=None):
        self.next=None
        self.data=data
    def insert(self,data:int):
        if self.data is None:
            self.data=data
            return self
        if self.next is None:
            self.next=List(data)
            return self.next
        return self.next.insert(data)
    def find(self,key:int):
        if self.data is None:
            return None
        if self.data==key:
            return self
        if self.next is not None:
            self.next.find(key)
        return None
    
    def remove(self,key:int):
        if self.data is None:
            return
        if self.next is None:
            return
        if self.next.data==key:
            self.next=self.next.next      
            return  
        return 

class Chain:
    def __init__(self,data:int=None):
        self.next=None
        self.list=List(data)
    def insert(self,data:int):
        if self.list is None:
            self.list=List(data)
            return self.list
        else:
            return self.list.insert(data)
        
    def find(self,key:int):
        if self.list is None:
            return None
        return self.list.find(key)
    
    def remove(self,key:int):
        if self.list is None:
            return
        if self.list.data==key:
            self.list=self.list.next
            return
        return self.list.remove(key)

class HashTable:
    def __init__(self,param:int=512):
        self.param=param
        self.arr=[]
        for i in range(param):
            self.arr.append(Chain())

    def __calc_hash(self,key:int):
        return key%self.param
    
    def insert(self,key:int):
        hash=self.__calc_hash(key)
        # Init chain
        self.arr[hash].insert(key)
    
    def find(self,key:int):
        hash=self.__calc_hash(key)
        return self.arr[hash].find(key)
    
    def remove(self,key:int):
        hash=self.__calc_hash(key)
        return self.arr[hash].remove(key)
    
