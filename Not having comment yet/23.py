import heapq

heap = []

# 模擬 list1 = [2, 6]、list2 = [1, 2, 3]
heapq.heappush(heap, (2, 0, 'node_2'))  # list1
heapq.heappush(heap, (1, 1, 'node_1'))  # list2

# 看看 heap 的內容
print(heap)
###^ heapq 本身就是最小堆，最小的元素會在最上面自動堆疊

# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_sort(lists: List[Optional[ListNode]]) -> List:
            n = len(lists)
            if n <= 1:
                return lists
            middle = n // 2
            left = merge_sort(lists[:middle])
            right = merge_sort(lists[middle:])
            return merge(left,right)

        def merge(left_linked_list: List, right_linked_list: List) -> List:
            i = 0
            j = 0
            left = left_linked_list[0]
            right = right_linked_list[0]
            res = []
            dummy = ListNode(0, None)
            pt = dummy
            while(left is not None and right is not None):
                if left.val <= right.val:
                    pt.next = ListNode(left.val, None)
                    pt = pt.next
                    left = left.next
                else:
                    pt.next = ListNode(right.val, None)
                    pt = pt.next
                    right = right.next
            if right is not None:
                pt.next = right
            else:
                pt.next = left
            res.append(dummy.next)
            return res
        res = merge_sort(lists)
        return res[0] if len(res) > 0 else None
                

#^ 這個程式碼是用merge sort的方式來合併k個linked list
