class Solution:
    def maxSubArray(self, nums):
          current = nums[0]
          maxsum = nums[0]

          for i in range(1,len(nums)):
            current = max(nums[i],current + nums[i])
            maxsum = max(maxsum,current)
          return maxsum