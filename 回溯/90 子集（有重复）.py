class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrace(i,temp):
            result.append(temp[:])
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                backtrace(j+1,temp+[nums[j]])
        backtrace(0, [])
        return result