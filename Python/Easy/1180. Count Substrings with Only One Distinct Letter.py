class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        count, repeat = 0,1
        
        for i in range(1,len(S)):
            if S[i]!=S[i-1]:
                count+=(repeat*(repeat+1))//2
                repeat=0
            repeat+=1
        return count+(repeat*(repeat+1))//2