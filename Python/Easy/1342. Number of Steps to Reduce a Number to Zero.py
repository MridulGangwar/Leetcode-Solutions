using recursion

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count=1
        
        if num==1:
            return 1
        elif num==0:
            return 0
        
        if num%2:
            count=count+self.numberOfSteps(num-1)
        else:
            count=count+self.numberOfSteps(num/2)
        
        return count
		
		
using iteration

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count=0
        while num>0:
            if num%2==0:
                num=num/2
            else:
                num=num-1
            count+=1
        return count