class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        x = len(nums) - k
        new = []
        for i in range(x,len(nums)):
            new.append(nums[i])
        for i in range(0,x):
            new.append(nums[i])
        nums[::] = new
        return nums
