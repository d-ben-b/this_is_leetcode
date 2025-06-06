# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,None)
        pt = dummy
        L1 = list1
        L2 = list2
        while(L1 != None and L2 != None):
            if L1.val < L2.val:
               pt.next = ListNode(L1.val,None)
               L1 = L1.next
            else:
                pt.next = ListNode(L2.val,None)
                L2 = L2.next
            pt = pt.next
        if L1:
            pt.next = L1
        elif L2:
            pt.next = L2
        # while(L1 != None):
        #     pt.next = ListNode(L1.val,None)
        #     L1 = L1.next
        #     pt = pt.next
        # while(L2 != None):
        #     pt.next = ListNode(L2.val,None)
        #     L2 = L2.next
        #     pt = pt.next
        #^ use while loop to add the rest of the list make the code run slower than the above

        return dummy.next