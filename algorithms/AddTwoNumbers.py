# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listToInteger(self,l):
        res = ""
        while l is not None:
            res += str(l.val)
            l = l.next
        return int(res[::-1])
    
    def integerToList(self,number):
        # index = None
        # if number == 0:
        #     index = ListNode(0)
        #     return index
        # else:
        listNode = None
        head = None
        for i in str(number)[::-1]:
            if listNode is None:
                listNode = ListNode(i)
                head = listNode
            else:
                listNode.next = ListNode(i)
                listNode = listNode.next
        return head
            
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res_1 = self.listToInteger(l1)
        res_2 = self.listToInteger(l2)
        return self.integerToList(res_1+res_2)
        