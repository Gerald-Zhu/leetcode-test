class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, track = [], []
        def backtrack(n, k, start, track, result):
            if len(track) == k:
                result.append(track[:])
            for i in range(start, n+1):
                track.append(i)
                backtrack(n, k, i+1, track, result)
                track.pop()
        backtrack(n, k, 1, track, result)
        return result