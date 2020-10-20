class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if not intervals or not intervals[0]:
            return True
        
        
        intervals.sort(key = lambda x:x[0])
        
        start, end = intervals[0][0], intervals[0][1]
        
        for interval in intervals[1:]:
            if interval[0]<end:
                return False
            start, end = interval[0], interval[1]
            
        return True
        
        
        