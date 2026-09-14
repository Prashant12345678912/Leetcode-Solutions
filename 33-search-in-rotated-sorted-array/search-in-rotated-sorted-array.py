class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=(s+e)//2
            if(nums[mid]==target):
                return mid
            elif(nums[s]<=nums[mid]):
                if(nums[s]<=target and target < nums[mid]):
                    e=mid-1
                else:
                    s=mid+1
            elif(nums[mid]<target and target<=nums[e]):
                s=mid+1
            else:
                e=mid-1
        return -1                       
        