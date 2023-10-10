class TrieNode:
    def __init__(self):
        self.word=None
        self.child={}
        pass

    def insert(self,prefix:str,word):
        if len(prefix)==0:
            self.word=word
            return 
        char=prefix[0]
        if char not in self.child:
            self.child[char]=TrieNode()
        self.child[char].insert(prefix[1:],word)

    def search(self,prefix:str,word):
        if len(prefix)==0:
            if self.word is None: return False
            return self.word==word
        char=prefix[0]
        if char not in self.child:
            return False
        return self.child[char].search(prefix[1:],word)
    def startsWith(self, prefix: str) -> bool:
        if len(prefix)==0:
            return True
        char=prefix[0]
        if char not in self.child:
            return False
        return self.child[char].startsWith(prefix[1:])

class Trie:
    def __init__(self):
        self.root=TrieNode()        

    def insert(self, word: str):
        self.root.insert(word,word)
        

    def search(self, word: str) -> bool:
        return self.root.search(word,word)
        

    def startsWith(self, prefix: str) -> bool:
        return self.root.startsWith(prefix)

a=Trie()
a.insert('abc')
print(a.search('abc'))      # True
print(a.search('abdc'))     # False
print(a.search('ab'))       # False
print()
print(a.startsWith('abc'))  # True
print(a.startsWith('abdc')) # False
print(a.startsWith('ab'))   # True

print()
trie =Trie();
trie.insert("apple");
print(trie.search("apple"));       # True
print(trie.search("app"));         # False
print(trie.startsWith("app"));     # True
trie.insert("app");
print(trie.search("app"));         # True