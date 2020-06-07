class Solution:

    def __init__(self, w: List[int]):
        self.array_sum =[]
        temp_sum = 0
        for num in w:
            temp_sum+=num
            self.array_sum.append(temp_sum)
        self.total_sum = temp_sum

    def pickIndex(self) -> int:
        index = random.randint(1,self.total_sum)
        left, right = 0 , len(self.array_sum)
        while left<right:
            mid = left + (right-left)//2
            if index>self.array_sum[mid]:
                left=mid+1
            else:
                right=mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()