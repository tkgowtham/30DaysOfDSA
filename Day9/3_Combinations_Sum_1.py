class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        subset = []

        def findS(index, sums, subset):
            if index == len(candidates):
                if sums == target:
                    result.append(subset.copy())
                return

            if sums + candidates[index] <= target:
                subset.append(candidates[index])
                findS(index, sums + candidates[index], subset)
                subset.pop()
            
            findS(index + 1, sums, subset)

        findS(0, 0, subset)
        return result
