class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        d = {}
        for i, x in enumerate(a):
            if t - x in d:
                return [d[t - x], i]
            d[x] = i
