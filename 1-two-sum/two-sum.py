class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # s = {}
        # for i,num in enumerate(nums):
        #     diff = target - num
        #     if diff in s:
        #         return [s[diff],i]
        #     else:
        #         s[num] = i
        # return []    








        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff],i]
            dic[nums[i]] = i 
        return []   