#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

from typing import List  # vscodeでList is not definedを回避する


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # enumerate:インデックス番号, 要素の順で取得可能
        # ↓ i=インデックス番号、main_nums=nums[i]の要素 が取得できる
        for i, main_num in enumerate(nums):
            diff_num = target - main_num

            # もしリストnumsにdiff_numが存在する(if 検索値 in List変数)
            # かつ
            # リストnumsにdiff_numがあるインデックス番号が現在のfor分での対象場所でない場合
            # インデックスの結果を返す
            if diff_num in nums and nums.index(diff_num) != i:
                return [i, nums.index(diff_num)]
        return
# @lc code=end
