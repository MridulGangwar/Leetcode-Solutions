class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        m,n = len(text1),len(text2)
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(n):
            for j in range(m):
                if text1[j]==text2[i]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
                    
        return dp[-1][-1]