class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left = 1
        right = sum(candies) // k
        
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            
            store = 0
            for i in candies:
                store += i // mid
            if store >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans 
