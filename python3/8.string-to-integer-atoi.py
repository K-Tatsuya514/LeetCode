#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# submit result
# 1084/1084 cases passed (52 ms)
# Your runtime beats 55.21 % of python3 submissions
# Your memory usage beats 79.5 % of python3 submissions (16.3 MB)

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # 先頭の空白削除
        s = s.lstrip()

        # 文字数が0の場合
        if len(s) == 0:
            return 0

        signed: bool = True  # 符号識別(true:正 false:負)

        # 先頭が+or-かを判断
        if s[0] == '-':
            signed = False
            s = s[1:]  # 先頭1文字目を削除する
        elif s[0] == '+':
            s = s[1:]  # 先頭1文字目を削除する

        judge_s: str = ''  # 一文字ずつ結合して数値か検査するための変数

        # 文字列がない場合は0を返す
        if len(s) == 0:
            return 0

        # 一文字ずつ処理
        for spell in s:
            if not self.is_int(judge_s+spell):
                if len(judge_s) == 0:  # 頭が数字でない場合は0を返す
                    judge_s = 0
                    return 0
                break
            else:
                judge_s += spell

        # 負の処理
        if not signed:
            judge_s = '-' + judge_s

        return_num: int = int(judge_s)

        # 32bit処理
        if return_num < -(2**31):
            return_num = -(2**31)

        if return_num >= 2**31:
            return_num = 2**31-1

        # 戻り値
        return return_num

    # 数値に変換可能か判断関数
    def is_int(self, s):  # 整数値を表しているかどうかを判定
        try:
            int(s)  # 文字列を実際にint関数で変換してみる
        except ValueError:
            return False
        else:
            return True


# @lc code=end
