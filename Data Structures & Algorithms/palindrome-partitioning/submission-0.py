class Solution:
    def isValid(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def backTrack(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isValid(s, i, j):
                    part.append(s[i:j + 1])
                    backTrack(j + 1)
                    part.pop()
        backTrack(0)
        return res