class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*(col+1) for i in range(row+1)]
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=1+min(dp[i][j],dp[i][j+1],dp[i+1][j])
                else:
                    dp[i+1][j+1]=0
        
        result=0
        for i in range(row+1):
            for j in range(col+1):
                if dp[i][j]>result:
                    result=dp[i][j]
                    
        return result**2