# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        protect = ListNode(0, head)
        last = protect
        while head != None:
            #1.分组（往后走k-1步，获取k个节点） 一组的开头和结尾

            end = Solution.get_K_end(head, k)
            if end == None:break
            next_group_head = end.next
            #2.组内进行翻转
            Solution.reverseList(head, next_group_head)
            #3.更新每一组和前一组的节点，后一组的节点
            last.next = end;
            head.next = next_group_head

            last = head;
            head = next_group_head
        return protect.next
        
    def get_K_end(head, k):
        while head != None:
            k += -1
            if k == 0:return head
            head = head.next
        # 分组不够K, 返回空
        return None
    
    #反转链表，不包含最后一个节点
    def reverseList(head, end):
        # 遍历整个链表
        pre = head
        head = head.next
        while head != end:
            #用一个临时变量储存下一个node
            temp = head.next
            #将当前node指向上一个节点
            head.next = pre
            # 翻转完成后 当前的head变成pre节点
            # head改变
            pre = head
            head = temp
        
