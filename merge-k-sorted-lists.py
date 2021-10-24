# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, l, r) -> ListNode:
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l+r) >> 1
        return self.mergeTwoLists(merge(lists, l, mid), merge(lists, mid+1, r))

    def mergeTwoLists(self, a:ListNode, b:ListNode)-> ListNode:
        if a == None and b == None:
            return None
        if a == None:
            return b
        if b == None:
            return a

        head = ListNode(0)
        tail = head
        aPtr = a
        bPtr = b
        while (aPtr != None and bPtr != None):
            if aPtr.val < bPtr.val:
                tail.next = aPtr
                aPtr = aPtr.next
            else:
                tail.next = bPtr
                bPtr = bPtr.next
            tail = tail.next
        if aPtr != None:
            tail.next = aPtr
        else:
            tail.next = bPtr
        return head.next 
