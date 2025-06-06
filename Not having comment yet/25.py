# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        pt = dummy
        def parseList(head: Optional[ListNode], k: int) -> Optional[ListNode]:
            pt = head
            value_table = []
            #print(f"NOW head is {head}")
            # check all value is all valid
            for i in range(k):
                if pt == None:
                    value_table = []
                    return head
                else:
                    value_table.append(pt.val)
                    pt = pt.next #point at new list
            #print(f"{pt=}")
            # reverse
            #print(f"{value_table[-1]=}")
            #print(f"{value_table[-2]=}")
            reverse_ptr = head
            for i in range(1, k + 1):
                reverse_ptr.val = value_table[-i]
                reverse_ptr = reverse_ptr.next
            reverse_ptr = parseList(pt, k)
            #print(f"{reverse_ptr=}")
            return head

        dummy.next = parseList(head, k)
        #print(f"{dummy=}")
        return dummy.next
                