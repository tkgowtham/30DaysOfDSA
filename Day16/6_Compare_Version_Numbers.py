class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        while len(v2) < len(v1):
            v2.append('0')
        while len(v2) > len(v1):
            v1.append('0')
        
        v1 = [int(i) for i in v1]
        v2 = [int(i) for i in v2]

        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        
        return 0
