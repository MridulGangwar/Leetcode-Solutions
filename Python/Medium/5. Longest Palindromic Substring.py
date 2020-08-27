class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.middle(s,i,i)
            len2 = self.middle(s,i,i+1)
            length = max(len1,len2)
            if length > end-start:
                start = i - ((length-1)//2)
                end  = i + ((length)//2)
        return s[start:end+1]
            
    def middle(self,s,left,right):
        if not s or left>right:
            return 0
        while left>=0 and right<=len(s)-1 and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
        
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestP, n = "", len(s)
        
        for i in range(n):
            first = self.middle(s,i,i)
            second = self.middle(s,i,i+1)
            if len(first)>len(second):
                temp = first
            else:
                temp= second
            if len(temp)>len(longestP):
                longestP = temp
                
        return longestP
            
    def middle(self,s,left,right):
        
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        
        return s[left+1:right]
            
        
        