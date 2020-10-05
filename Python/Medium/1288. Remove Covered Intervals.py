class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : (x[0],-x[1]))
        result=0
        
        for interval in intervals:
            if result>0:
                if interval[0]>=start and interval[1]<=end:
                    pass
                else:
                    start, end = interval[0],interval[1]
                    result+=1
            else:
                start, end = interval[0],interval[1]
                result+=1
            
        return result