##approach 1

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        dic={}
        s = set()
        o = set(range(1,N+1))
        
        if len(trust) < N-1:
            return -1
        
        if N==1 and len(trust)==0:
            return N
        
        for t in trust:
            s.add(t[0])
            if t[1] not in dic:
                dic[t[1]]=1
            else:
                dic[t[1]]+=1
                
        for i in o-s:
            if i in dic:
                if dic[i]==N-1:
                    return i
        
        return -1
		
##approach 2

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if len(trust) < N-1:
            return -1
        
        arr = [0]*(N+1)
        
        for a,b in trust:
            arr[a]-=1
            arr[b]+=1
            
        for idx,val in enumerate(arr[1:],1):
            if val==N-1:
                return idx
            
        return -1