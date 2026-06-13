class Solution:
    def func(self, ind, nums, res):
        if ind == len(nums):
            res.append(nums[:])
            return
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            self.func(ind + 1, nums, res)
            nums[ind], nums[i] = nums[i], nums[ind]

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.func(0, nums, res)
        return res