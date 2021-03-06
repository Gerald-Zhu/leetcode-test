class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0: return []
        used = [False for _ in range(size)]
        res = []
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth+1, path, used, res)
                    used[i] = False
                    path.pop()
        dfs(nums, size, 0, [], used, res)
        return res


"""
DFS深度优先搜索
"""