#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# submit result
# 93/93 cases passed (1195 ms)
# Your runtime beats 5.08 % of python3 submissions
# Your memory usage beats 14.37 % of python3 submissions (16.6 MB)

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        word_list = list(s)

        # 文字列sが奇数の時点でFalseを返す
        if len(word_list) % 2 == 1:
            return False

        # Open bracketに対応するClose bracketの辞書
        dict_brackets = {'(': ')', '{': '}', '[': ']'}

        # 検索対象のbracketの範囲を考えるための変数(リスト形式)
        edge = [len(word_list)]

        for i, word in enumerate(word_list):
            # Open bracketとClose bracketの組み合わせが正しいことを判断する変数
            comb_open = 0  # Open bracketの判断番号
            comb_close = 0  # Close bracketの判断番号

            # すでに組み合わせを確認済みのclose bracketをfor分wordである場合はスキップ
            if i == edge[-1]:
                edge.pop(-1)
                continue

            # 検索対象がClose bracketの場合はFalseを返す
            if word not in dict_brackets.keys():
                return False

            # for分word(Open bracket)に対するClose bracketを検索
            for j in range(i+1, edge[-1]):

                # 検索対象のOpen bracket内に、他のOpen bracketが存在した場合、組み合わせ判定の変数を+1する
                if word == word_list[j]:
                    comb_open += 1

                # Close bracketが存在したら、for分を抜けて、対象括弧内に他括弧がないかの検索に進む
                elif dict_brackets[word] == word_list[j]:

                    # bracketの組み合わせの正負
                    if comb_open == comb_close:
                        edge.append(j)  # 確認済みの閉じ括弧のインデックス番号をリストに追加
                        break
                    else:
                        comb_close += 1

            # 閉め括弧が存在しなかったら、その時点でFalseを返す
            else:
                return False

        return True


# @lc code=end
