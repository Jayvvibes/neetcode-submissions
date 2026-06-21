class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x
        res = 0
        while l <= h:
            mid = (l + h) // 2
            if mid * mid > x:
                h = mid - 1
            elif mid * mid < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res
