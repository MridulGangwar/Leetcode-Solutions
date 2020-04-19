class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        first_element = grid[0][0]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if i==0 and j<len(grid[i])-1:
                    grid[i][j+1]+=grid[i][j]
                elif i>0 and j==0:
                    grid[i][j]+=grid[i-1][j]
                elif i>0 and j>0:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
                    
        return grid[len(grid)-1][len(grid[0])-1]