# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(2N) O(1) , TC cannot be improved from stack based approach, SC reduced from using stack O(N).
class Solution:
    def reverse(self, head):
        temp = head
        prev = None
        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse(slow)

        while head != None and slow != None:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next

        return True
