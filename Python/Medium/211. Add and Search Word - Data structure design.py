class TreeNode:
    def __init__(self,val):
        self.val =val 
        self.children = {}
        self.endhere = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        parent = self.root
        for i, ch in enumerate(word):
            if ch not in parent.children:
                parent.children[ch] = TreeNode(ch)
            parent = parent.children[ch]
        parent.endhere = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(i,current):
            
            if i == len(word):
                return current.endhere
            
            ch = word[i]
            if ch in current.children:
                return dfs(i+1,current.children[ch])
            elif ch==".":
                for key in current.children.keys():
                    if dfs(i+1,current.children[key]):
                        return True
                return False
            else:
                return False
        
        return dfs(0,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)