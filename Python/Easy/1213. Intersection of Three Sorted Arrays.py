class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        
        i,j,k = 0,0,0
        n1,n2,n3 = len(arr1),len(arr2),len(arr3)
        result = []
        
        while(i<n1 and j < n2 and k<n3):
            
            if arr1[i]==arr2[j] and arr2[j]==arr3[k]:
                result.append(arr1[i])
                i+=1
                j+=1
                k+=1
            elif arr1[i] < arr2[j]:
                i+=1
            elif arr2[j] < arr3[k]:
                j+=1
            else:
                k+=1
        
        return result
                
                
        