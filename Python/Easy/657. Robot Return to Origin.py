class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        coord = [0,0]
        
        for i in moves:
            if i =='U':
                coord[1]+=1
            elif i =='D':
                coord[1]-=1
            elif i =='R':
                coord[0]+=1
            else:
                coord[0]-=1
        
        if coord[0]==0 and coord[1]==0:
            return 1
        else:
            return 0