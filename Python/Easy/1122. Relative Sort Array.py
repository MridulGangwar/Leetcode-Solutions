class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result=[0]*len(arr1)
        
        dic_num = {}
        
        for num in arr1:
            if num not in dic_num:
                dic_num[num]=1
            else:
                dic_num[num]+=1
        
        index=0
        for num in arr2:
            for j in range(dic_num[num]):
                result[index]=num
                index+=1
            del dic_num[num]
        
        for left_num in  sorted(dic_num.keys()):
            for j in range(dic_num[left_num]):
                result[index]=left_num
                index+=1
            
        print(dic_num)
        return result