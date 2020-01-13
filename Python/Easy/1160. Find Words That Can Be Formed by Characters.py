class Solution(object):
    def create_dic(self,char):
        d={}
        for i in char:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return d
    
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dic_chars=self.create_dic(chars)
        result=0
        for word in words:
            dic_word = self.create_dic(word)
            count=0
            for key in dic_word:
                if key in dic_chars and dic_word[key] <= dic_chars[key]:
                    count+=1
                if count==len(dic_word):
                    result+=len(word)
            
        return result