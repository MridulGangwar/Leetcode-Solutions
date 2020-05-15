class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.children={}
        self.endhere=False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        parent = self.root
        for i,char in enumerate(word):
            if char not in parent.children:
                parent.children[char]=TreeNode(char)
            parent=parent.children[char]
            if i==len(word)-1:
                parent.endhere=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return parent.endhere

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)