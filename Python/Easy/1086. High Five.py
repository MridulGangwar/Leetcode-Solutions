from collections import defaultdict

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        
        temp = defaultdict(list)
        
        for i in items:
            temp[i[0]].append(i[1])
            
        return ([k,sum(sorted(temp[k],reverse=True)[:5])/5] for k in temp.keys())
            