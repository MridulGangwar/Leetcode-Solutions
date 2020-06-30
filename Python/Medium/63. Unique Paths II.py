#Method 1
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        if m==0:
            return 0
        n = len(obstacleGrid[0])
        
        dp = [[0]*(n) for _ in range(m)]
        
        for j in range(n):
            if obstacleGrid[0][j]==1:
                break
            dp[0][j]=1
                
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                    
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]
		
#Method 2
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        if m==0:
            return 0
        n = len(obstacleGrid[0])
        
        dp = [[0]*(n) for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    continue
                    
                if i==0 and j==0:
                    dp[0][0]=1
                
                if i>0:
                    dp[i][j]+=dp[i-1][j]
                if j>0:
                    dp[i][j]+=dp[i][j-1]
                
        return dp[m-1][n-1]