class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        index=0
        
        while index<len(S)-1:
            if S[index]==S[index+1]:
                S = S[:index] + S[index+2:]
                if index!=0:
                    index-=1
            else:
                index+=1
            
        return S    
            
        