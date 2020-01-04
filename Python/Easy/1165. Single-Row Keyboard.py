class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        key = {}
        
        for i in range(len(keyboard)):
            key[keyboard[i]] = i
            
        prev,current,dist=0,0,0
        
        for i in word:
            current = key[i]
            dist = dist+abs(current-prev)
            prev = current
    
        return dist