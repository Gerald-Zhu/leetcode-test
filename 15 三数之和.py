class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = []
        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            c = n - 1
            for b in range(a + 1,n):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                while b < c and nums[b] + nums[c] > -nums[a]:
                    c -= 1
                if b == c:
                    break
                if nums[b] + nums[c] == -nums[a]:
                    output.append([nums[a],nums[b],nums[c]])
        return output

"""
ByteDance 2020.9 first interview
"""