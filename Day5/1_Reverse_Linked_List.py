# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(N) Approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev

#Recursive Approach O(N)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head

        newHead = self.reverseList(head.next)

        front = head.next
        front.next = head
        head.next = None

        return newHead
