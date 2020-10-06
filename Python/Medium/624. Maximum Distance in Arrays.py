class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        minn,maxn = arrays[0][0], arrays[0][len(arrays[0])-1]
        res = 0
        
        for i in range(1,len(arrays)):
            array = arrays[i]
            res = max(res,max(abs(maxn-array[0]),abs(array[len(array)-1]-minn)))
            minn = min(minn,array[0])
            maxn = max(maxn,array[len(array)-1])
        
        return res