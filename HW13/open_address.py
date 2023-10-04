
class HashTable:
    def __init__(self,param:int=2):
        self.param=param     

        self.arr=[None]*(param)        

    def __calc_hash(self,key:int):        
        return key%self.param        
    
    def __find_key_place(self,arr,hash,key:int):
        if arr[hash] is None:
            return hash
        if arr[hash][0]==key:
            return hash        
        
        for i in range (hash,len(arr)):
            if arr[i] is not None:
                if arr[i][0]==key:
                    return i
                else:
                    continue
            if arr[i] is None:
                return i
        
        # Если мы тут значит места свободного не осталось в массиве и был достигнут его конец - значит нужно расширять
        self.__enlarge()
        return self.__find_key_place(self.arr,hash,key)
            
    def __enlarge(self,multiplier:int=2):
        self.param=self.param*multiplier
        new_arr=[None]*(self.param)

        for i in self.arr:
            if i is None:
                continue
            hash=self.__calc_hash(i[0])
            pos=self.__find_key_place(new_arr,hash,i[0])
            if new_arr[pos] is None:
                new_arr[pos]=i    
        self.arr=new_arr 


    def insert(self,key:int):
        hash=self.__calc_hash(key)
        # Init chain
        pos=self.__find_key_place(self.arr,hash,key)
        if self.arr[pos] is None:
            self.arr[pos]=[key,1]    
            return 
        self.arr[pos]=[key,self.arr[pos][1]+1]
    
    def find(self,key:int):
        hash=self.__calc_hash(key)
        if self.arr[hash] is None:
            return None
        if self.arr[hash][1] == 0:
            return None
        else:
            return self.arr[hash][0]
    
    def remove(self,key:int):
        hash=self.__calc_hash(key)
        self.arr[hash]=[key,self.arr[hash][1]-1]
        return self.arr[hash]
    