class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0 , len(s)-1
        self.reverse(s,l,r)
        i,n = 0,len(s)
        while i<n:
            j = i+1
            while j<n and s[j]!=" ":
                j+=1
            
            self.reverse(s,i,j-1)
            i=j+1
    
    def reverse(self,s,l,r):
        while l<=r:
            s[l],s[r]=s[r],s[l]
            r-=1
            l+=1
        return s