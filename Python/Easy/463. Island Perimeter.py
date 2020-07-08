class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        if grid is None or len(grid)==0 or len(grid[0])==0:
            return 0
        
        result=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col]==1:
                    
                    result+=4
                
                    if row>0 and grid[row-1][col]==1:
                        result-=2
                    
                    if col>0 and grid[row][col-1]==1:
                        result-=2
                    
        return result