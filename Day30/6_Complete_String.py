class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')]

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()

    def checkIfPrefixExist(self,word):
        flag = True
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                flag = flag
            if node.isEnd() == False:
                return False
        return True


def completeString(n: int, a: List[str])-> str:
    
    # Write your Code here
    trie = Trie()
    for ch in a:
        trie.insert(ch)

    longest = ""
    for ch in a:
        if (trie.checkIfPrefixExist(ch)):
            if len(ch) > len(longest):
                longest = ch
            elif len(ch) == len(longest) and ch < longest:
                longest = ch

    if not longest:
        return None

    return longest
