# -*- coding: utf-8 -*-
# @Time        : 2019/11/29 11:22
# @Author      : tianyunzqs
# @Description : 


def edit_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i

    for j in range(1, n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[-1][-1]


if __name__ == '__main__':
    s1 = 'ABCDEF'
    s2 = 'AABCEF'
    print(edit_distance(s1, s2))
