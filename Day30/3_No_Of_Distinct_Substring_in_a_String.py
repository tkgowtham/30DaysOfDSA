class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag

def countDistinctSubstrings(s):
    root = Node()
    cnt = 0
    n = len(s) 
    for i in range(n):
        node = root
        for j in range(i, n):
            if not node.containsKey(s[j]):
                node.put(s[j], Node())
                cnt += 1
            node = node.get(s[j])
    
    return cnt + 1
