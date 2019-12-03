# -*- coding: utf-8 -*-
# @Time        : 2019/12/3 10:27
# @Author      : tianyunzqs
# @Description : 字典树


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
            p[""] = ""

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
        elif isinstance(trie, str):
            res.append(s)
            return trie

    res = []
    fun(trie, '')
    return res


if __name__ == '__main__':
    tree = gen_trie('dict.txt')
    print(tree)
    print(print_trie_words(tree))
    add_word_to_trie('电钻', tree)
    print(tree)
    print(print_trie_words(tree))
    add_word_to_trie('手电钻子', tree)
    print(tree)
    print(print_trie_words(tree))
    delete_word_from_trie('手电钻', tree)
    print(tree)
    print(print_trie_words(tree))
    delete_word_from_trie('电钻', tree)
    print(tree)
    print(print_trie_words(tree))
