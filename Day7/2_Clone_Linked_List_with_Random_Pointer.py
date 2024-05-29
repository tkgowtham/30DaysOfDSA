"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#TC -> O(2N) SC -> O(N) + O(N) hashmap used This approach more efficient in terms of both time and memory as compared to the next.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
            
        dict1 = {}
        temp = head
        while temp != None:
            newNode = Node(temp.val)
            dict1[temp] = newNode
            temp = temp.next

        temp = head
        while temp != None:
            copiedNode = dict1[temp]
            try:
                copiedNode.next = dict1[temp.next]
            except KeyError:
                copiedNode.next = None

            try:
                copiedNode.random = dict1[temp.random]
            except KeyError:
                copiedNode.random = None
            temp = temp.next

        return dict1[head]


#O(3N) O(N)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp != None:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next

        temp = head
        while temp != None:
            copyNode = temp.next
            try:
                copyNode.random = temp.random.next
            except AttributeError:
                copyNode.random = None
            temp = temp.next.next

        dummy = Node(-1)
        res = dummy
        temp = head
        while temp != None:
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next

        return dummy.next
