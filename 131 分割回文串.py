class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    backtrack(s[i:], tmp + [s[:i]])
        backtrack(s, [])
        return res