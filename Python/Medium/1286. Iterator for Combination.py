from collections import deque
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.poll = deque()
        
        def recursive(st,idx,combinationLength):
            if len(st)==combinationLength:
                self.poll.append(st)
            else:
                for i in range(idx,len(characters)):
                    st = st+characters[i]
                    recursive(st,i+1,combinationLength)
                    st = st[:-1]
        recursive("",0,combinationLength)
        
    def next(self):
        return self.poll.popleft()
        
    def hasNext(self):
        return self.poll


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()



from collections import deque
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def recursive(st,idx,length):
            
            if length==0:
                self.combination.append(st)    
            else:
                if idx>=len(characters):
                    return
                else:
                    recursive(st+characters[idx],idx+1,length-1)
                    recursive(st,idx+1,length)
            
        self.combination = collections.deque()
        recursive("",0,combinationLength)
        
        
    def next(self) -> str:
        return self.combination.popleft()

    def hasNext(self) -> bool:
        return self.combination 


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()