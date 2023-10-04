
class HashTable:
    def __init__(self,quadratic_param:int=1):
        self.arr=[None]*(1)      
        self.quadratic_param=quadratic_param   

    def __calc_hash(self,key:int,arr):
        size=len(arr)
        pos=key%size
        if arr[pos] is None:
            return pos
        if arr[pos][0] == key:
            return pos     
        for i in range(size):   
            pos_quad=(pos+i*i)%size
            if arr[pos_quad] is None:
                return pos_quad
            if arr[pos_quad][0] == key:
                return pos_quad
        # раз мы здесь значит не получилоь найти ни одну позицию свободную
        return None         
    
            
            
    def __enlarge(self,arr,multiplier:int=2):
        size=len(arr)
        new_arr=[None]*(size*multiplier)

        for i in arr:
            if i is None:
                continue            
            hash=self.__calc_hash(i[0],new_arr)
            if new_arr[hash] is None:
                new_arr[hash]=i    
        return new_arr 



    def insert(self,key:int):
        hash=self.__calc_hash(key,self.arr)
        while hash is None:
            self.arr=self.__enlarge(self.arr)
            hash=self.__calc_hash(key,self.arr)
        # Init chain
        if self.arr[hash] is None:
            self.arr[hash]=[key,1]    
            return 
        self.arr[hash]=[key,self.arr[hash][1]+1]
    
    def find(self,key:int):
        hash=self.__calc_hash(key,self.arr)
        if self.arr[hash] is None:
            return None
        if self.arr[hash][1] == 0:
            return None
        else:
            return self.arr[hash][0]
    
    def remove(self,key:int):
        hash=self.__calc_hash(key,self.arr)
        self.arr[hash]=[key,self.arr[hash][1]-1]
        return self.arr[hash]
    