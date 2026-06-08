class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for num, freq in count.items():
            if freq > len(nums) // 3:
                res.append(num)
        return res