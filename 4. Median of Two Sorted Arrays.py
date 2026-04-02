class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)  # merge and sort
        n = len(merged)
        mid = n // 2
        
        if n % 2 == 0:
            return (merged[mid-1] + merged[mid]) / 2
        else:
            return merged[mid]
