# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode(-1,None)
        temp = dummy
        while temp1 != None and temp2 != None:
            if temp1.val < temp2.val:
                dummy.next = temp1
                temp1 = temp1.next
            else:
                dummy.next = temp2
                temp2 = temp2.next
            dummy = dummy.next

        while temp1 != None:
            dummy.next = temp1
            temp1 = temp1.next
            dummy = dummy.next

        while temp2 != None:
            dummy.next = temp2
            temp2 = temp2.next
            dummy = dummy.next

        return temp.next
