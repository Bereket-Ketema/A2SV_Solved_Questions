class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        store = []
        for i in nums:
            if i in store:
                store.remove(i)
            else:
                store.append(i)
        return store[0]
