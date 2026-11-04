class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        uniq = []
        for i in nums:
            if  i != val:
                uniq.append(i)
        nums[::] = uniq
        return len(uniq)
        