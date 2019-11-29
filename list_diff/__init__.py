# -*- coding: utf-8 -*-
# @Time        : 2019/11/29 18:21
# @Author      : tianyunzqs
# @Description : 比较两个列表的相似度

import re
import difflib


def list_diff(list1: list, list2: list):
    """
    寻找两个list的异同点，并返回其下标
    :param list1:
    :param list2:
    :return:
    """
    list1_diff, list2_diff = [], []
    diff = difflib._mdiff(list1, list2)

    found_diff_num = 0
    for from_line, to_line, found_diff in diff:
        if found_diff:
            found_diff_num += 1
            if from_line[1] == '\n':
                list1_diff.append({'txt': '', 'idx': []})
            else:
                from_line_parts = re.split(r'(\x00[-\^].*?\x01)', from_line[1])
                tmp_txt, tmp_idx, ind = '', [], 0
                for part in from_line_parts:
                    if not part:
                        continue
                    if re.search(r'^\x00[-\^].*\x01$', part):
                        part_text = part.strip('\x00-').strip('\x00\^').strip('\x01')
                        tmp_idx.append([ind, ind + len(part_text)])
                    else:
                        part_text = part
                    tmp_txt += part_text
                    ind += len(part_text)
                list1_diff.append({'txt': tmp_txt, 'idx': tmp_idx})

            if to_line[1] == '\n':
                list2_diff.append({'txt': '', 'idx': []})
            else:
                to_line_parts = re.split(r'(\x00[\+\^].*?\x01)', to_line[1])
                tmp_txt, tmp_idx, ind = '', [], 0
                for part in to_line_parts:
                    if not part:
                        continue
                    if re.search(r'^\x00[\+\^].*\x01$', part):
                        part_text = part.strip('\x00\+').strip('\x00\^').strip('\x01')
                        tmp_idx.append([ind, ind + len(part_text)])
                    else:
                        part_text = part
                    tmp_txt += part_text
                    ind += len(part_text)
                list2_diff.append({'txt': tmp_txt, 'idx': tmp_idx})
        else:
            list1_diff.append({'txt': from_line[1], 'idx': []})
            list2_diff.append({'txt': to_line[1], 'idx': []})

    return {
        'is_same': found_diff_num == 0,
        'diff1_idx': list1_diff,
        'diff2_idx': list2_diff,
        'list1': list1,
        'list2': list2,
        'sim_score': found_diff_num / len(list1_diff) if list1_diff else 0.0
    }


if __name__ == '__main__':
    d1 = [
        '广州汽车展览',
        '林书豪缅怀高以翔',
        '人民日报高狄逝世'
    ]
    d2 = [
        '北京汽车展览时间发布',
        '人民日报高狄逝世'
    ]
    print(list_diff(d1, d2))
