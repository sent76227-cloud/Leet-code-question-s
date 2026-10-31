class Solution(object):
    def merge(self, nums1, m, nums2, n):

        new = []
        i = 0
        j  = 0
        k = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i = i+1
            else:
                new.append(nums2[j])
                j = j+1
        while i < m:
               new.append(nums1[i])
               i=i+1
        while j < n:
            new.append(nums2[j])
            j = j+1
        nums1[::] = new
        return nums1

