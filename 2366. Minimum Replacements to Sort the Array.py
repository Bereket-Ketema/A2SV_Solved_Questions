class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        val = nums[-1]
        for i in range(len(nums)-2, -1, -1):
                part = ceil(nums[i] / float(val))
                res += part - 1
                val = nums[i] // part
        return res   
