from heapq import *
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        self.minHeap, self.maxHeap = [], [] 
        self.result = [0]*(len(nums)-k+1)
        
        for i in range(len(nums)):
            num = nums[i]
            
            if not self.maxHeap or -self.maxHeap[0]>num:
                heappush(self.maxHeap,-num)
            else:
                heappush(self.minHeap,num)
                
            self.balance()
            
            if i-k+1>=0:
                self.calculatemedian(i-k+1)
                itemToBeDeleted = nums[i-k+1]
                if itemToBeDeleted>-self.maxHeap[0]:
                    self.remove(self.minHeap,itemToBeDeleted)
                else:
                    self.remove(self.maxHeap,-itemToBeDeleted)
                    
                self.balance()
                
        return self.result
    
        
    def balance(self):
        if len(self.maxHeap)>len(self.minHeap)+1:
            heappush(self.minHeap,-heappop(self.maxHeap))
        elif len(self.maxHeap)<len(self.minHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))
            
    def calculatemedian(self,idx):
        if len(self.maxHeap)==len(self.minHeap):
            self.result[idx]=(-self.maxHeap[0]+self.minHeap[0])/2
        else:
            self.result[idx]=-self.maxHeap[0]
            
    def remove(self,heap,n):
        idx = heap.index(n)
        heap[idx]=heap[-1]
        del heap[-1]
        
        heapify(heap)