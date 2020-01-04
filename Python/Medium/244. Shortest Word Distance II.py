from collections import defaultdict

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.orDict = defaultdict(list)
        
        for i,word in enumerate(words):
            self.orDict[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_index = self.orDict[word1]
        word2_index = self.orDict[word2]
        
        dist = float("inf")
        for w1 in word1_index:
            for w2 in word2_index:
                temp = abs(w2-w1)
                if temp<dist:
                    dist=temp
        
        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)