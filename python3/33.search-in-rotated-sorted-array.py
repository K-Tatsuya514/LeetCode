#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# submit result
# 195/195 cases passed (63 ms)
# Your runtime beats 22.23 % of python3 submissions
# Your memory usage beats 6.91 % of python3 submissions (16.8 MB)

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


# @lc code=end
