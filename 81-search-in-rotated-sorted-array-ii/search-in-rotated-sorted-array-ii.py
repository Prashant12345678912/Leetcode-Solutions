class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        s=0
        e=len(nums)-1

        while s<=e:
            mid = s+(e-s)//2
            if nums[mid] == target:
                return True
            if nums[s] == nums[mid] and nums[mid] == nums[e]:
                s+=1
                e-=1
            elif nums[s]<=nums[mid]:
                if nums[s]<=target<nums[mid]:
                    e = mid-1
                else:
                    s = mid+1
            elif nums[mid]<target<=nums[e]:
                s=mid+1
            else:
                e=mid-1
        return False                 