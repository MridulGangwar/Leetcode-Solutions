class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()
        self.length = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.length+=1
        while t-self.queue[0]>3000:
            self.queue.popleft()
            self.length-=1
        
        return self.length
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)