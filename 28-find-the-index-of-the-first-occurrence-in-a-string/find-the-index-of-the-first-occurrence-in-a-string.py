class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)

        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1

        n=len(haystack)
        m=len(needle)
        if(len(needle)==0):
            return -1
        
        for i in range(n-m+1):
            j=0
            while(j<m and haystack[i+j]==needle[j]):
                j+=1
            if(j == m):
                return i
        return -1

