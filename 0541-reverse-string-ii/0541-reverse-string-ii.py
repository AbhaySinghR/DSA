class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        if len(s)<k:
            return s[::-1]

        