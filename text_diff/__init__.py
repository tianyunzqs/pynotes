# -*- coding: utf-8 -*-
# @Time        : 2019/11/29 17:38
# @Author      : tianyunzqs
# @Description : 文本差异性比较

import difflib


def text_diff(string1: str, string2: str):
    # 获取string1和string2各自不同位置
    string1_diff, string2_diff = [], []
    d = difflib.Differ()  # 创建Differ对象
    diff = list(d.compare(string1, string2))  # 采用compare方法对字符串进行比较

    tmp = [-1, -1]
    i, diff_len = 0, len(diff)
    idx1, idx2 = 0, 0

    while i < diff_len - 1:
        if diff[i][0] == '-':
            if tmp[0] == -1:
                tmp[0] = idx1

            idx1 += 1
            tmp[1] = idx1
            if diff[i + 1][0] != '-':
                string1_diff.append(tmp)
                tmp = [-1, -1]

        elif diff[i][0] == '+':
            if tmp[0] == -1:
                tmp[0] = idx2

            idx2 += 1
            tmp[1] = idx2
            if diff[i + 1][0] != '+':
                string2_diff.append(tmp)
                tmp = [-1, -1]

        else:
            idx1 += 1
            idx2 += 1

        i += 1

    if diff:
        if diff[-1][0] == '-':
            if tmp[0] == -1:
                tmp = [len(string1) - 1, len(string1)]
            else:
                tmp[1] = len(string1)
            string1_diff.append(tmp)

        elif diff[i][0] == '+':
            if tmp[0] == -1:
                tmp = [len(string2) - 1, len(string2)]
            else:
                tmp[1] = len(string2)
            string2_diff.append(tmp)

    return {
        'is_same': not string1_diff and not string2_diff,
        'diff1_idx': string1_diff,
        'diff2_idx': string2_diff,
        'string1': string1,
        'string2': string2,
        'sim_score': difflib.SequenceMatcher(None, string1, string2).ratio()
    }


if __name__ == '__main__':
    s1 = '中国的首都是北京'
    s2 = '北京是中国的首都'
    print(text_diff(s1, s2))
