# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 遍历整个链表
        pre = None
        while head != None:
            #用一个临时变量储存下一个node
            temp = head.next
            #将当前node指向上一个节点
            head.next = pre
            # 翻转完成后 当前的head变成pre节点
            # head改变
            pre = head
            head = temp
        return pre