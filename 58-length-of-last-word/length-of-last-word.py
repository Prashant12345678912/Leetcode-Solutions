class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        j=0
        i = len(s)-1
        for i in range(i,-1,-1):
            if(s[i]==' '):
                if(j>0):
                    return j
                else:
                    continue
            else:
                j+=1
        return j