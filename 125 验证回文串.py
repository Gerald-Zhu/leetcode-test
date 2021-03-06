class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall(re.compile(r'[A-Za-z0-9]+'), s)).lower()
        return s == s[::-1]