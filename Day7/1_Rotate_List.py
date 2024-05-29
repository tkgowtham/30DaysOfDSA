# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head

        length = 1
        temp = head
        while temp.next != None: #Going to end of LL and calc length
            temp = temp.next
            length += 1

        temp.next = head #Join the last to head
        k = k % length #Calc no of rotations
        end = length - k #find end node if rotated
        while end > 0:
            temp = temp.next #Going till that node
            end -= 1

        head = temp.next # Making it as head
        temp.next = None

        return head 
