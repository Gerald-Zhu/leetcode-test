class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newnum = nums1 + nums2
        newnum.sort()
        if len(newnum) % 2 == 0:
            return (newnum[int(len(newnum)/2 - 1)]+newnum[int(len(newnum)/2)])/2
        else:
            return newnum[int((len(newnum)+1)/2)-1]