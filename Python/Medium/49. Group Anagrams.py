from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        orDict = defaultdict(list) 
        result=[]
        
        for st in strs:
            sort_st = ''.join(sorted(st))
            orDict[sort_st].append(st)
            
        for key in orDict:
            result.append(orDict[key])
            
        return result
        