class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #first solution
        
        #odd_num=[]
        #even_num=[]
        
        #for i in A:
        #    if i%2==0:
        #        even_num.append(i)
        #    else: odd_num.append(i)
                
        #odd_index,even_index,index=0,0,0
        #result=[]
        
        #while odd_index<len(odd_num) or even_index<len(even_num):
        #    if index%2==0:
        #        result.append(even_num[even_index])
        #        even_index+=1
        #    else:
        #        result.append(odd_num[odd_index])
        #        odd_index+=1
        #    index+=1
            
        #return result
        
        #second solution
        result=[0]*len(A)
        odd_index,even_index=1,0
        
        for i in A:
            if i %2==0:
                result[even_index]=i
                even_index+=2
            else:
                result[odd_index]=i
                odd_index+=2
        
        return result