class Solution:
    def func(self, ind, total, nums, res, subset, target):
        if total == target:
            res.append(list(subset))
            return
        if ind >= len(nums) or total >  target:
            return
        subset.append(nums[ind])
        self.func(ind, total + nums[ind], nums, res, subset, target)
        subset.pop()
        self.func(ind + 1, total, nums, res, subset, target)
        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        self.func(0, 0, nums, res, subset, target)
        return res