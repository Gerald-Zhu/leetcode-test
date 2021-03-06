class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        if m == 1:
            return matrix[0];
        if n == 1:
            return [m[0] for m in matrix]
        ret = matrix[0] + [m[-1] for m in matrix[1:]] + matrix[-1][-2::-1] + [m[0] for m in matrix[-2:0:-1]]
        return ret + self.spiralOrder([m[1:-1] for m in matrix[1:-1]])
