#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# submit result
# 208/208 cases passed (60 ms)
# Your runtime beats 15.61 % of python3 submissions
# Your memory usage beats 14.53 % of python3 submissions (16.5 MB)

# vscodeで*** is not definedを回避する
from typing import Optional
from typing import List


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Linked list を配列arrayに変形する
        array_list1: List = self.__get_list(list1)
        array_list2: List = self.__get_list(list2)

        # 並列に変更後、list1とlist2を結合する
        array_list3 = array_list1 + array_list2

        # 戻り値のlist3
        list3 = None

        # 配列のsortedを利用してソート後、linked listの形に戻す
        for c in sorted(array_list3):
            # list3がNone=はじめの場合
            if list3 is None:
                list3 = ListNode(c)
            else:
                current = list3
                while current.next is not None:
                    current = current.next
                current.next = ListNode(c)

        return list3

    # Linked list を配列arrayに変形する
    def __get_list(self, list_item):
        current = list_item
        array_list = []
        while current is not None:
            array_list.append(current.val)
            current = current.next

        return array_list

# @lc code=end
