class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def recursive(comb,idx,target):
            if target==0:
                result.append(list(comb))
                return
            elif target<0:
                return
            else:
                for i in range(idx,n):
                    comb.append(candidates[i])
                    recursive(comb,i,target-candidates[i])
                    comb.pop()
            
            
        result,n = [], len(candidates)
        recursive([],0,target)
        return result