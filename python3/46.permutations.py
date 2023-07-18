#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# submit result
# 26/26 cases passed (51 ms)
# Your runtime beats 82.7 % of python3 submissions
# Your memory usage beats 93.08 % of python3 submissions (16.4 MB)

# @lc code=start
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)

# @lc code=end
