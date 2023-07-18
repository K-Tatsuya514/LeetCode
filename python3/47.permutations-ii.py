#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# submit result
# 33/33 cases passed (76 ms)
# Your runtime beats 56.45 % of python3 submissions
# Your memory usage beats 79.99 % of python3 submissions (16.6 MB)

# @lc code=start
import itertools


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(itertools.permutations(nums))

# @lc code=end
