class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc]==newColor:
            return image
        
        self.fill(image,sr,sc,image[sr][sc],newColor)
        return image
    
    def fill(self,image,i,j,color,newColor):
        if i<0 or i>len(image)-1 or j<0 or j>len(image[0])-1 or image[i][j]!=color:
            return
        
        image[i][j]=newColor
        self.fill(image,i-1,j,color,newColor)
        self.fill(image,i+1,j,color,newColor)
        self.fill(image,i,j-1,color,newColor)
        self.fill(image,i,j+1,color,newColor)