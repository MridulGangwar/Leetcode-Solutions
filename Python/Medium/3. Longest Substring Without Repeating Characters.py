class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        ws,result,mapS =-1,0,{}
        for we in range(len(s)):
            
            if s[we] in mapS and mapS[s[we]]>ws:
                ws = mapS[s[we]]
            else:
                result = max(result,we-ws)
            mapS[s[we]] =we
            
        return result
        