#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# submit result
# 987/987 cases passed (2063 ms)
# Your runtime beats 5.01 % of python3 submissions
# Your memory usage beats 13.02 % of python3 submissions (16.5 MB)

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_word = []  # 検索対象で使用している文字列を格納していく
        longest = 0  # 戻り値

        # 文字列sの先頭文字を減らしていき、無くなるまで繰り返す
        while s:

            # 文字列sを一文字ずつ処理していく
            for ch in s:

                # 文字が重複時に行う処理
                if ch in check_word:
                    rep_word = ''.join(check_word)  # 配列内の要素つなぎ合わせて文字列に変換
                    check_word = []  # 配列初期化
                    s = s[1:]  # 先頭1文字目を削除する

                    # longestの更新
                    if longest < len(rep_word):
                        longest = len(rep_word)

                    break
                else:
                    check_word.append(ch)

            # longestが残りの検索文字数より大きい場合処理終了
            if len(s) <= longest:
                break

        return longest


# @lc code=end
