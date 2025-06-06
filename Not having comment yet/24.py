# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        pt = dummy

        def parse_lists(head: Optional[ListNode]) -> Optional[ListNode]:
            #print(head)
            if head == None or head.next == None:
                return head
            else:
                left = head
                right = head.next
                left.val ^= right.val
                right.val ^= left.val
                left.val ^= right.val
            #print(f"this is the first head {head=}")
            head.next.next = parse_lists(head.next.next)
            #print(f"{head.next.next=}")
            return head
        dummy.next = parse_lists(head)
        #print(f"this is res {dummy=}")
        return dummy.next