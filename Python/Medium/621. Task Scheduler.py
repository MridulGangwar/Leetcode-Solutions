class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n==0:
            return len(tasks)
        
        char_map = [0]*26
        for task in tasks:
            char_map[ord(task)-ord('A')]+=1
            
        char_map.sort()
        maxE = char_map[25]-1
        idleTime = maxE*n
        
        for i in range(24,-1,-1):
            idleTime-=min(maxE,char_map[i])
            if idleTime<=0:
                return len(tasks)
            
        return idleTime+len(tasks)