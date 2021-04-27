# -*- coding: utf-8 -*-
# @Time        : 2019/12/3 10:27
# @Author      : tianyunzqs
# @Description : 字典树

import copy


def gen_trie(path):
    """
    构建词典树
    :param path: 词典路径
    :return:
    """
    trie = dict()
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip()
            p = trie
            for w in word:
                if w not in p:
                    p[w] = {}
                p = p[w]
            p[""] = word

    return trie


def is_word_in_trie(word, trie):
    """
    判断word是否在词典树trie中
    :param word: 待判定的词
    :param trie: 词典树
    :return: 在，返回True；不在，返回False
    """
    p = trie
    for w in word:
        if w not in p:
            return False
        else:
            p = p[w]
    if "" in p:
        return True
    else:
        return False


def extract_words(text, trie, return_all=True):
    """
    在输入文本text中抽取trie中的词语
    :param text: 输入文本
    :param trie: 词典树
    :param return_all: 是否返回所有在词典树中的词语（包含位置重叠）
    :return: 词语及其下标
    """
    result = []
    N = len(text)
    i, j = 0, 0
    p = trie
    while i < N:
        c = text[j]
        if c in p:
            p = p[c]
            if '' in p:
                if return_all:
                    result.append((p[''], i, j + 1))
                else:
                    if len(p) == 1:
                        result.append((p[''], i, j + 1))
                        i = j
                    else:
                        if j + 1 >= N or text[j + 1] not in p:
                            result.append((p[''], i, j + 1))
                            i = j
            j += 1
            if j >= N:
                i += 1
                j = i
                p = trie
        else:
            p = trie
            i += 1
            j = i
    return result


def get_word_from_trie(word, trie, default=None):
    """
    获取word在词典树trie中所对应的值，如果不存在，则返回default
    :param word: 待判定的词
    :param trie: 词典树
    :param default: 默认返回值
    :return: 在，返回对应的值；不在，返回default
    """
    p = trie
    for w in word:
        if w not in p:
            return default
        else:
            p = p[w]
    if "" in p:
        return p[""]
    else:
        return default


def set_word_value_in_trie(word, trie, value):
    """
    设置word在词典树trie中所对应的值，如果不存在，则无修改
    :param word: 待判定的词
    :param trie: 词典树
    :param value: 设置值
    :return:
    """
    p = trie
    for w in word:
        if w not in p:
            return
        else:
            p = p[w]
    if "" in p:
        p[""] = value
    else:
        return


def add_word_to_trie(word, trie):
    """
    新增词语到字典树中
    :param word: 待新增词语
    :param trie: 字典树
    :return: 新增词语后的字典树
    """
    p = trie
    for w in word:
        if w not in p:
            p[w] = {}
        p = p[w]
    p[""] = ""


def delete_word_from_trie(word, trie):
    """
    删除字典树中词语，如果存在则删除，否则原样返回
    :param word: 待删除词语
    :param trie: 字典树
    :return: 删除词语后的字典树
    """
    p = trie
    delete_flag = [False] * len(word)
    for i, w in enumerate(word):
        if w not in p:
            return
        else:
            p = p[w]
            delete_flag[i] = True if len(p) <= 1 else False
    if "" in p:
        if len(p) > 1:
            p.pop('')
            return
        p = trie
        for i, flag in enumerate(delete_flag):
            if not flag:
                p = p[word[i]]
            else:
                p.pop(word[i])
                break
    else:
        return


def two_trie_combine(trie1, trie2):
    """
    将两个字典树trie1和trie2进行合并，并返回合并后的字典树
    :param trie1: 字典树
    :param trie2: 字典树
    :return: 合并后的字典树
    """
    def fun(trie, s, trie12):
        if isinstance(trie, dict):
            for k, v in trie.items():
                fun(v, s + k, trie12)
        elif isinstance(trie, str):
            add_word_to_trie(s, trie12)
            return trie

    trie_combine = copy.deepcopy(trie1)
    fun(trie2, '', trie_combine)
    return trie_combine


def print_trie_words(trie):
    """
    输出字典树中所有词语
    :param trie: 字典树
    :return: 字典树中所有词语列表
    """
    def fun(trie, s):
        if isinstance(trie, dict):
            for k, v in trie.items():
                fun(v, s + k)
        else:
            res.append(s)
            return trie

    res = []
    fun(trie, '')
    return res


if __name__ == '__main__':
    tree = gen_trie('dict2.txt')
    print(tree)
    print(print_trie_words(tree))

    is_contain = is_word_in_trie('电钻', tree)
    print(is_contain)

    text = "冲击钻头"
    all_words = extract_words(text, tree, return_all=False)
    print(all_words)

    # add_word_to_trie('电钻', tree)
    # print(tree)
    # print(print_trie_words(tree))
    # add_word_to_trie('手电钻子', tree)
    # print(tree)
    # print(print_trie_words(tree))

    # delete_word_from_trie('手电钻', tree)
    # print(tree)
    # print(print_trie_words(tree))
    # delete_word_from_trie('电钻', tree)
    # print(tree)
    # print(print_trie_words(tree))

    word_value = get_word_from_trie('电钻', tree, default='未找到该词')
    print(word_value)

    # set_word_value_in_trie('木工钻', tree, 123)
    # print(tree)
    # print(print_trie_words(tree))

    # tree1 = gen_trie('dict.txt')
    # tree2 = gen_trie('dict2.txt')
    # print(tree1)
    # print(print_trie_words(tree1))
    # print(tree2)
    # print(print_trie_words(tree2))
    #
    # tree_combine = two_trie_combine(tree1, tree2)
    # print(tree_combine)
    # print(print_trie_words(tree_combine))

    # print(tree1)
    # print(print_trie_words(tree1))
    # print(tree2)
    # print(print_trie_words(tree2))
