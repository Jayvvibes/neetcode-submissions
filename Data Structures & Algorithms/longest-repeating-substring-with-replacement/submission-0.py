class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        charset = {}
        maxFreq = 0
        maxLen = 0
        while r < len(s):
            charset[s[r]] = 1 + charset.get(s[r], 0)
            maxFreq = max(maxFreq, charset[s[r]])
            if (r - l + 1) - maxFreq > k:
                charset[s[l]] -= 1
                maxFreq = 0
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen