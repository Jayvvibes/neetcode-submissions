class Solution:
    def func(self, ind, total, target, nums, res, subset):
        if total == target:
            res.append(list(subset))
            return
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            if total + nums[i] > target:
                break
            subset.append(nums[i])
            self.func(i + 1, total + nums[i], target, nums, res, subset)
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        self.func(0, 0, target, candidates, res, subset)
        return res
    