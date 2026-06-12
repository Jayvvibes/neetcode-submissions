class Solution:
    def func(self, ind, nums, subset, res):
        if ind >= len(nums):
            res.append(list(subset))
            return
        subset.append(nums[ind])
        self.func(ind + 1, nums, subset, res)
        subset.pop()
        self.func(ind + 1, nums, subset, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.func(0, nums, subset, res)
        return res