# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        temp1 = l1
        temp2 = l2

        carry = 0
        while temp1 != None or temp2 != None or carry > 0:
            val = 0
            if temp1 != None:
                val += temp1.val
                temp1 = temp1.next
            if temp2 != None:
                val += temp2.val
                temp2 = temp2.next
            val += carry
            node_val = val % 10
            dummy.next = ListNode(node_val)
            dummy = dummy.next
            carry = int(val // 10)
        
        return temp.next
