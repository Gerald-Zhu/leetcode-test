class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = 0
        for i in range(n):
            tmp = tmp ^ nums[i]
        return tmp