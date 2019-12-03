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


if __name__ == '__main__':
    print(gen_trie('dict.txt'))
