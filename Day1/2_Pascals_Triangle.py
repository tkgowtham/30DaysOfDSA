class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        l = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = [1,1]
            last = l[len(l) - 1]
            for j in range(0,len(last)-1):
                temp.insert(1,last[j]+last[j+1])
            l.append(temp)

        return l
