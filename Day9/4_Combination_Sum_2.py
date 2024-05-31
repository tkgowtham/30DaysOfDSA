class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        subset = []

        def findS(index, sums, subset):
            if sums == target:
                result.append(subset.copy())
                return

            if sums > target or index == len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                findS(i + 1, sums + candidates[i], subset)
                subset.pop()

        findS(0, 0, subset)
        return result
