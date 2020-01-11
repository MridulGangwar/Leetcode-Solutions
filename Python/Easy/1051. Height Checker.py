class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights_sorted = sorted(heights)
        counts=0
        
        for i in range(len(heights)):
            if heights[i]!=heights_sorted[i]:
                counts+=1
        return counts
        