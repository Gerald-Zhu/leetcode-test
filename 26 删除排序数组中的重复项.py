class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        l, r = 0, 0
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1