class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        init_d ={}
        for i in A[0]:
            if i not in init_d:
                init_d[i]=1
            else: init_d[i]+=1
    
        for i in range(1,len(A)):
            temp={}
            for char in A[i]:
                if char not in temp and char in init_d:
                    temp[char]=1
                elif char in temp and char in init_d:
                    temp[char]+=1
                   
            for i in init_d.keys():
                if i not in temp:
                    del init_d[i]
                else:
                    init_d[i] = min(init_d[i],temp[i])
        
        result=[]
        for key in init_d.keys():
            for i in range(init_d[key]):
                result.append(key)
                
        return result