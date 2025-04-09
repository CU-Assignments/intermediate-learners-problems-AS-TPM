class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l = r = res = 0
        while r < len(s):
            if s[r] in m:
                l = max(l, m[s[r]] + 1)
            m[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res
