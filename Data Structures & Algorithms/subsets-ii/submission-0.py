class Solution:
    def func(self, ind, nums, res, subset):
        if ind == len(nums):
            res.add(tuple(subset))
            return
        subset.append(nums[ind])
        self.func(ind + 1, nums, res, subset)
        subset.pop()
        self.func(ind + 1, nums, res, subset)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        subset = []
        self.func(0, nums, res, subset)
        return [list(s) for s in res]