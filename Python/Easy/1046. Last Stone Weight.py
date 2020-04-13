class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = sorted(stones)
        
        while len(stones)>1:
            top = stones[-1]
            second_top = stones[-2]
            
            stones.pop()
            stones.pop()
            
            if top>second_top:
                stones.append(top-second_top)
            stones = sorted(stones)
            
            
        if len(stones)==1:
            return stones[0]
        else:
            return 0