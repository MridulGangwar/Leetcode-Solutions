class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        points.sort(key = lambda x:x[0])
        start, end, result = points[0][0],points[0][1], 1
        
        for point in points:
            if end >= point[0]:
                end = min(end,point[1])
            else:
                start, end = point[0], point[1]
                result+=1
                
        return result
        