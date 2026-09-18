class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        n = x
        sum = 0
        while(x!=0):
            rem = x%10
            x = x//10
            sum = sum*10+rem
        if(sum == n):
            return True
        else:
            return False
