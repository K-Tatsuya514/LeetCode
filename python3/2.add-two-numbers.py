#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# submit result
# 1568/1568 cases passed (73 ms)
# Your runtime beats 87.65 % of python3 submissions
# Your memory usage beats 30.55 % of python3 submissions (16.5 MB)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_l1: int = self.__get_num(l1)
        num_l2: int = self.__get_num(l2)

        num_sum = list(str(num_l1 + num_l2))

        l3 = None
        for c in num_sum:
            n = ListNode(c)
            n.next = l3
            l3 = n

        return l3

    def __get_num(self, list_item):
        current = list_item
        num = ""
        while current is not None:
            num += str(current.val)
            current = current.next

        return int(num[::-1])

# @lc code=end
