#TC = O(2^n) SC = O(n * 2^n)
def wordBreak(s, dictionary):

    # Write your code here
    if len(s) == 0:
        return []

    ans = []
    store = {} #set
    def solve(index):
        if index in store:
            return store[index]
        if index == len(s):
            return [[]]

        result = []
        for end in range(index + 1, len(s) + 1):
            word = s[index:end]
            if word in dictionary:
                for subsentence in solve(end):
                    result.append([word] + subsentence)
        
        store[index] = result
        return result

    res = solve(0)
    ans = [" ".join(word) for word in res]
    return ans
