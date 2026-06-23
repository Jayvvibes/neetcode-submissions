class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = high

        def canShip(cap, days):
            d_days = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    d_days += 1
                    if d_days > days:
                        return False
                    currCap = cap
                currCap -= w
            return d_days <= days

        while low <= high:
            mid = (low + high) // 2
            if canShip(mid, days):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res