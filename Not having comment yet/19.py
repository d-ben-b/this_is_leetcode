from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         print(f'{head=}')
#         counter = 0
#         target = head
#         p = head
#         while(p.next != None):
#             print(f'{head=}')
#             p = p.next
#             if counter == n:
#                 target = target.next
#             else:
#                 counter += 1
#         target.next = p 
#         return head
##^ 這個方法會有問題 沒有dummy node的話 沒辦法處理刪除head的情況
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while(fast):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
