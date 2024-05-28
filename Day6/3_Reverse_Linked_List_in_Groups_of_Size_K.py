# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthNode(temp, k):
            while temp != None and k > 0:
                k -= 1
                temp = temp.next
            return temp

        dummy = ListNode(0)
        dummy.next = head
        prevLast = dummy

        while True:
            kthNode = getKthNode(prevLast, k)
            if kthNode == None:
                break

            nextNode = prev = kthNode.next
            curr = prevLast.next

            while curr != nextNode:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prevLast.next
            prevLast.next = kthNode
            prevLast = temp

        return dummy.next
