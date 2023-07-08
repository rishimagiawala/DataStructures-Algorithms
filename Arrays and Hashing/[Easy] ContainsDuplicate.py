class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        ---->O(n^2) Time Complexity, not ideal
        for i in range(len(nums)):
            for l in range(len(nums)):
                if l != i and nums[i] == nums[l]:
                 return True
        return False
        """

        """
        ---->O(nlogn) due to sorting, 
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
        """
        numSet = set()

        for i in range(len(nums)):
            if nums[i] in numSet:
                return True
            else:
                numSet.add(nums[i])

        return False
        