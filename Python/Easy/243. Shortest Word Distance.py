from collections import defaultdict

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        orDict = defaultdict(list)
        
        for i,word in enumerate(words):
            orDict[word].append(i)
        
        word1_index = orDict[word1]
        word2_index = orDict[word2]
        
        dist = float("inf")
        for w1 in word1_index:
            for w2 in word2_index:
                dist=min(dist,abs(w2-w1))        
        
        return dist
        