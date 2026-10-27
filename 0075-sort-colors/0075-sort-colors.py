class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1

        index = 0
        for i in range(freq.get(0,0)):
            nums[index] = 0
            index+=1
        for i in range(freq.get(1,0)):
             nums[index] = 1
             index+=1
        for i in range(freq.get(2,0)):
              nums[index] = 2
              index+=1