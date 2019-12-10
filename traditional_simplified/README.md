# 简繁体互转
简繁体互转工具参考来源：[https://github.com/skydark/nstools/blob/master/zhtools/langconv.py](https://github.com/skydark/nstools/blob/master/zhtools/langconv.py)<br/> 

繁体中文转简体中文<br/>
```python
def traditional2simplified(sentence):
    """
    将句子中所有繁体字转换为简体字
    :param sentence: 待转换文本
    :return: 将句子中繁体字转换为简体字后的文本
    """
    return Converter('zh-hans').convert(sentence)

[in]: 中華人民共和國
[out]: 中华人民共和国
```

简体中文转繁体中文<br/>
```python
def simplified2traditional(sentence):
    """
    将句子中所有简体字转换为繁体字
    :param sentence: 待转换文本
    :return: 将句子中简体字转换为繁体字后的文本
    """
    return Converter('zh-hant').convert(sentence)
    
[in]: 中华人民共和国
[out]: 中華人民共和國
```