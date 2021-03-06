class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        mul_list = [1]
        for i in range(1, n):
            mul_list.append(mul_list[-1] * i)
        ans = []
        mod = k-1
        nums = list(range(1, n+1))
        for mul in mul_list[::-1]:
            div, mod = divmod(mod, mul)
            ans.append(str(nums.pop(div)))
        return "".join(ans)