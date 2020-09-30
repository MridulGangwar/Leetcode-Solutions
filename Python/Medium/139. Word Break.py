class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    
        return self.helper(s,wordDict,{})
    
    def helper(self,s,wordDict,memory):
        
        if len(s)==0:
            return True
        elif s in memory:
            return memory[s]
        
        for word in wordDict:
            if s.startswith(word) and self.helper(s[len(word):],wordDict,memory):
                memory[s]=True
                return True
        
        memory[s]=False
        return False
    