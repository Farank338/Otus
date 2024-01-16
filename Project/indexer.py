
class Index:
    def __init__(self):
        self.tree={}
        self.words={}
    

    def insert(self,word:str,data):
        if len(word)>1:
            char=word[0]
            if char not in self.tree:
                self.tree[char]=Index()
            self.tree[char].insert(word[1:],data)
            return
        
        if word in self.words:
            self.words[word]=self.words[word]+data
        else:
            self.words[word]=data
        return
    
    def search(self,word):
        if len(word)>1:
            char=word[0]
            if char not in self.tree:
                return None
            return self.tree[char].search(word[1:])
        if word in self.words:
            return self.words[word]
        return None
def merge(*args):
    data={}
    if  len(args)<=1: return data
    for k in 

a=Index()
a.insert("abc",[0,1,2,3])
a.insert("abc1",[1,2,3])
a.insert("abc",[1,2,3])
a.insert("abc2",[1,2,3,4])
merge(a.search("abc"),a.search("abc2"))

