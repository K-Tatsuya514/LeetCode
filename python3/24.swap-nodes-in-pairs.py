#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# submit result
# 55/55 cases passed (51 ms)
# Your runtime beats 33.76 % of python3 submissions
# Your memory usage beats 5.59 % of python3 submissions (16.5 MB)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        array_list = []

        current = head
        while current is not None:
            array_list.append(current.val)
            current = current.next

        for i, num in enumerate(array_list):
            if i % 2 == 0 and i+1 != len(array_list):
                array_list[i] = array_list[i+1]
                array_list[i+1] = num
            else:
                continue

        # 戻り値のreturn_list
        return_list = None

        # 配列をlinked listの形に戻す
        for c in array_list:
            # return_listがNone=はじめの場合
            if return_list is None:
                return_list = ListNode(c)
            else:
                current = return_list
                while current.next is not None:
                    current = current.next
                current.next = ListNode(c)

        return return_list

# @lc code=end
