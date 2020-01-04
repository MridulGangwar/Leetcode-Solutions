from collections import defaultdict

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        orDict = defaultdict(list)
        
        for i,word in enumerate(words):
            orDict[word].append(i)
        
        word1_index = orDict[word1]
        word2_index = orDict[word2]
        
        dist = float("inf")
        for w1 in word1_index:
            for w2 in word2_index:
                temp = abs(w2-w1)
                if temp<dist and w1!=w2:
                    dist=temp
        
        
        return dist
        