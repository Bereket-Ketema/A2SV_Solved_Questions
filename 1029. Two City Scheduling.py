class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        store = []
        for c1, c2 in costs:
            store.append([c2 - c1, c1, c2])
        store.sort()
        result = 0
        for i in range(len(store)):
            if i < len(store) // 2:
                result += store[i][2]
            else:
                result += store[i][1]
        return result
