"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        if not schedule:
            return []
        
        stack = []
        for emp in schedule:
            for time in emp:
                stack.append(time)
                
        stack.sort(key = lambda x:x.start)
        
        start,end  = stack[0].start, stack[0].end
        overlaped_time = []
        
        for temp in stack[1:]:
            if temp.start<=end:
                end=max(end,temp.end)
            else:
                overlaped_time.append(Interval(start,end))
                start = temp.start
                end = temp.end
                
        
        overlaped_time.append(Interval(start,end))
        
        result=[]
        
        for idx in range(1,len(overlaped_time)):
            result.append(Interval(overlaped_time[idx-1].end,overlaped_time[idx].start))
            
        return result