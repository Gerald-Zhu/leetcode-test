class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        for i in range(len(digits) - 1):
            if digits[i] == 0: count += 1
            else: break
        digits = digits[count:]
        n = str(int(''.join([str(m) for m in digits])) + 1)
        return [0] * count + [int(i) for i in n]
