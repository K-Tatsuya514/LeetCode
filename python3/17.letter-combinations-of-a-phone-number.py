#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

# submit result
# 25/25 cases passed (43 ms)
# Your runtime beats 80.71 % of python3 submissions
# Your memory usage beats 56.24 % of python3 submissions (16.4 MB)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 入力する文字のリスト
        num_list = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], [
            'm', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        return_list: list = []  # 戻り値

        # 入力数値に対して1文字ずつ処理実行
        for num in digits:
            new_list: list = []

            if return_list == []:
                return_list = num_list[int(num)-2]
                continue

            for return_item in return_list:
                for num_item in num_list[int(num)-2]:
                    new_item = return_item + num_item
                    if not new_item in return_list:
                        new_list.append(return_item + num_item)

            return_list = new_list
            # print(return_list)

        return return_list

# @lc code=end
