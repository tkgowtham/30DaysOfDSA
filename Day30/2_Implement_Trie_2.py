class Node:
    def __init__(self):
        self.links = [None] * 26
        self.cntEndsWith = 0
        self.cntPrefix = 0

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def increase_end(self):
        self.cntEndsWith += 1

    def increase_prefix(self):
        self.cntPrefix += 1

    def delete_end(self):
        self.cntEndsWith -= 1

    def reduce_prefix(self):
        self.cntPrefix -= 1

class Trie:
    def __init__(self):
        # Write your code here.
        self.root = Node()
        pass

    def insert(self, word):
        # Write your code here.
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
            node.increase_prefix()
        node.increase_end()
        pass

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.cntEndsWith

    def countWordsStartingWith(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.cntPrefix

    def erase(self, word):
        # Write your code here.
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                node.reduce_prefix()
            else:
                return
        node.delete_end()
        pass
