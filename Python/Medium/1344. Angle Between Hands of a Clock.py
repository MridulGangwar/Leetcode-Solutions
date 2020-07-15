class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hd = hour*30+0.5*minutes
        md = 6*minutes
        diff = abs(hd-md)
        
        return min(diff,360-diff)