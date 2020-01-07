class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count=0
        left=0
        result =""
        for i in range(len(S)):
            if S[i]=='(':
                if count==0:
                    left=i+1
                count+=1
            else:
                count-=1
                
            if count==0:
                result+=S[left:i]
            
        return result
                
        