class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []

        if len(s) == 1:
            return [[s]]

        def isPalindrome(s):
            l1 = list(s)
            l2 = l1.copy()
            l2.reverse()
            if l1 == l2:
                return True
            else:
                return False

        def helper(index, s, path, result):
            if index == len(s):
                result.append(path.copy())
                return

            for i in range(index, len(s)):
                if isPalindrome(s[index:i+1]):
                    path.append(s[index: i + 1])
                    helper(i + 1, s, path, result)
                    path.pop()
            
        result = []
        path = []
        helper(0, s, path, result)
        return result
