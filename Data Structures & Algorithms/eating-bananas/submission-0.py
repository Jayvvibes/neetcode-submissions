class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = max(piles)
        while low <= high:
            mid = (low + high) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / mid)
            if total_time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res