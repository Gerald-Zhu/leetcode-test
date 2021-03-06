class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i, temp, res):
            res.append(temp)
            for j in range(i, n):
                backtrack(j+1, temp + [nums[j]], res)
        backtrack(0, [], res)
        return res