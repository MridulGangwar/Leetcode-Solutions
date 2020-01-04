class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        withoutVowels = [i for i in S.lower() if i not in vowels]
        
        return ''.join(withoutVowels)