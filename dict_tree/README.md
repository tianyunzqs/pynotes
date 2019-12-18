> 字典树又称单词查找树，Trie树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。
它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。

> 字典树有如下三个性质：
> 1.根节点不包含字符，除根节点外每一个节点都只包含一个字符;
> 2.从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串;
> 3.每个节点的所有子节点包含的字符都不相同。

本文中字典树的实现借鉴于jieba分词(之前版本，现jieba分词已升级为前缀树)。

字典树可应用于字符串检索、排序等。本文实现的字典树主要用于字符串检索，查找出字典中哪些词语在给定字符串中。该数据结构主要优点是随着词典的不断扩充，其查询时间复杂度不会明显增加，针对汉语常用字符也就3500多个，而英语就26个字母。

本文中的示例代码主要提供以下功能：

|功能|函数名|说明|
:---:|:---:|:---:
|构建字典树|```gen_trie```|构建词典树|
|查询|```is_word_in_trie```|判断word是否在词典树trie中|
|新增|```add_word_to_trie```|新增词语到字典树中|
|删除|```delete_word_from_trie```|删除字典树中词语，如果存在则删除，否则原样返回|
|合并|```two_trie_combine```|将两个字典树trie1和trie2进行合并，并返回合并后的字典树|
|set方法|```set_word_value_in_trie```|设置word在词典树trie中所对应的值，如果不存在，则无修改|
|get方法|```get_word_from_trie```|获取word在词典树trie中所对应的值，如果不存在，则返回default|
> 注：修改功能可通过删除和新增组合来实现，同时还提供了展示字典树所有词语的功能。

为了更好地可视化说明，我们先定义一个字典树输出函数```print_trie_words```，该函数主要是输出字典树中所有的词语。
```python
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
```

# 1.构建字典树
从文件中读入字符串构建字典树，文件中每一行表示一个词语，示例文件dict.txt中内容如下：
>木工钻<br/>
>手摇钻<br/>
>手电钻<br/>
>冲击钻<br/>

```python
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
```
```python
tree = gen_trie('dict.txt')
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
```
# 2.查询
查询给定词语 word 是否存在于某棵字典树 trie 中，如果存在，返回True；否则返回False
```python
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
```
```python
tree = gen_trie('dict.txt')
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
is_contain = is_word_in_trie('电钻', tree)
print(is_contain)
# [out]: False
```

# 3.新增
将给定词语 word 插入已存在的字典树 trie 中。
```python
def add_word_to_trie(word, trie):
    """
    新增词语到字典树中
    :param word: 待新增词语
    :param trie: 字典树
    :return: 
    """
    p = trie
    for w in word:
        if w not in p:
            p[w] = {}
        p = p[w]
    p[""] = ""
```
```python
tree = gen_trie('dict.txt')
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
add_word_to_trie('电钻', tree)
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}, '电': {'钻': {'': ''}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻', '电钻']
add_word_to_trie('手电钻子', tree)
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': '', '子': {'': ''}}}}, '冲': {'击': {'钻': {'': ''}}}, '电': {'钻': {'': ''}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '手电钻子', '冲击钻', '电钻']
```

# 4.删除
删除字典树 trie 中词语 word ，如果 trie 中存在 word，则在 trie 中删除 word，否则不作处理。
```python
def delete_word_from_trie(word, trie):
    """
    删除字典树中词语，如果存在则删除，否则原样返回
    :param word: 待删除词语
    :param trie: 字典树
    :return: 
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
```
```python
tree = gen_trie('dict.txt')
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
delete_word_from_trie('手电钻', tree)
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '冲击钻']
delete_word_from_trie('电钻', tree)
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '冲击钻']
```

# 5.get方法
获取词语 word 在词典树 trie 中所对应的值，如果不存在，则返回default
```python
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
```
```python
tree = gen_trie('dict.txt')
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
word_value = get_word_from_trie('电钻', tree, default='未找到该词')
print(word_value)
# [out]: 未找到该词
```

# 6.set方法
设置给定词语 word 在字典树 trie 中所对应的值，如果不存在，则无修改。
```python
def set_word_value_in_trie(word, trie, value):
    """
    设置word在字典树trie中所对应的值，如果不存在，则无修改
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
```
```python
tree = gen_trie('dict.txt')
print(tree)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
set_word_value_in_trie('木工钻', tree, 123)
print(tree)
# [out]: {'木': {'工': {'钻': {'': 123}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
```

# 7.合并
将两个字典树 trie1 和 trie2 进行合并，并返回合并后的字典树。
```python
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
```
dict.txt中内容如下：
>木工钻<br/>
>手摇钻<br/>
>手电钻<br/>
>冲击钻<br/>

dict2.txt中内容如下：
>木工钻<br/>
>钻头<br/>
>手电<br/>
>电钻<br/>
>冲击钻头<br/>
```python
tree1 = gen_trie('dict.txt')
tree2 = gen_trie('dict2.txt')
print(tree1)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}}}, '冲': {'击': {'钻': {'': ''}}}}
print(print_trie_words(tree1))
# [out]: ['木工钻', '手摇钻', '手电钻', '冲击钻']
print(tree2)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '钻': {'头': {'': ''}}, '手': {'电': {'': ''}}, '电': {'钻': {'': ''}}, '冲': {'击': {'钻': {'头': {'': ''}}}}}
print(print_trie_words(tree2))
# [out]: ['木工钻', '钻头', '手电', '电钻', '冲击钻头']
tree_combine = two_trie_combine(tree1, tree2)
print(tree_combine)
# [out]: {'木': {'工': {'钻': {'': ''}}}, '手': {'摇': {'钻': {'': ''}}, '电': {'钻': {'': ''}, '': ''}}, '冲': {'击': {'钻': {'': '', '头': {'': ''}}}}, '钻': {'头': {'': ''}}, '电': {'钻': {'': ''}}}
print(print_trie_words(tree_combine))
# [out]: ['木工钻', '手摇钻', '手电钻', '手电', '冲击钻', '冲击钻头', '钻头', '电钻']
```