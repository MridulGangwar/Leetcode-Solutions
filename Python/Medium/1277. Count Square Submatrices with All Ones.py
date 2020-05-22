class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m==0:
            return 0
        
        n = len(matrix[0])
        result=0
        mat = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]==1:
                    mat[i][j] = 1 + min(mat[i][j-1],mat[i-1][j],mat[i-1][j-1])
                    result+=mat[i][j]
                    
        return result
        
		
		
		
		
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m==0:
            return 0
        
        n = len(matrix[0])
        result=0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    if i==0 or j==0:
                        result+=1
                    else:
                        matrix[i][j] = 1 + min(matrix[i][j-1],matrix[i-1][j],
                                               matrix[i-1][j-1])
                        result+=matrix[i][j]
                    
        return result