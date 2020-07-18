import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = Counter(nums)
        
        bucket = []
        for num,freq in freq_map.items():
            if len(bucket)<k:
                heapq.heappush(bucket,(freq,num))
            else:
                min_freq,min_num = heapq.heappop(bucket)
                if freq>min_freq:
                    heapq.heappush(bucket,(freq,num))
                else:
                    heapq.heappush(bucket,(min_freq,min_num))
                    
        return [k for _,k in bucket]
                    