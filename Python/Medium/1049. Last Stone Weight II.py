class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        comb = {0}
        for stone in stones:
            temp=set()
            for i in comb:
                temp.add(abs(stone-i))
                temp.add(abs(stone+i))
                
            comb = temp
        return min(comb)