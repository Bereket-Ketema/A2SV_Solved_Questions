from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = Counter(s)
        count = 0
        for let in t:
          if let in freq:
            freq[let] -= 1
            if freq[let] == 0:
               del freq[let]
          else:
             count += 1
        return count
