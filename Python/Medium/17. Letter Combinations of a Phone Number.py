class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def recursive(idx,comb,mapping):
            if idx==len(digits):
                result.append(comb)
                return
            else:
                for ch in mapping[int(digits[idx])]:
                    comb+=ch
                    recursive(idx+1,comb,mapping)
                    comb = comb[:-1]
        
        result=[]
        mapping = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if digits:
            recursive(0,"",mapping)
        return result