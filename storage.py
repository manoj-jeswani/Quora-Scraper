 class TrieNode:
     
    def __init__(self):
        self.children = [None]*27
 
        # isLeaf is True if node represent the end of the word
        self.isLeaf = False
 
class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
     
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        # Converts key current character into index
        # use only 'a' through 'z' and lower case and hyphen
         
        if ch=='-':
            return 26
        else: 
            return ord(ch)-ord('a')
 
 
    def insert(self,key):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isLeaf = True
 
    def search(self, key):
         
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return pCrawl != None and pCrawl.isLeaf
 
