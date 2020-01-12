class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size=size
        self.value=[]
        

    def next(self, val: int) -> float:
        
        if len(self.value)==self.size:
            del self.value[0]
        
        self.value.append(val)
        
        return sum(self.value)/len(self.value)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)