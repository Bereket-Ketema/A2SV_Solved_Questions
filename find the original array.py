from collections import Counter

class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        count = Counter(changed)
        original = []

        for x in changed:
            if count[x] == 0:
                continue

            if count[2*x] == 0:
                return []

            count[x] -= 1
            count[2*x] -= 1
            original.append(x)

        return original
