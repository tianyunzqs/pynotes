# 列表差异性比较
利用python自带difflib包，比较输入的两个字符列表的差异性<br/>
列表差异性得分的计算比较粗暴，直接取两个列表差异元素的个数除以两个列表并集元素的个数<br/>
```python
[in1]: [
        '广州汽车展览',
        '林书豪缅怀高以翔',
        '人民日报高狄逝世'
    ]
[in2]:  [
        '北京汽车展览时间发布',
        '人民日报高狄逝世'
    ]
[out]: {
            'is_same': False, 
            'diff1_idx': [
                {'txt': '广州汽车展览', 'idx': [[0, 6]]}, 
                {'txt': '林书豪缅怀高以翔', 'idx': [[0, 8]]}, 
                {'txt': '人民日报高狄逝世', 'idx': []}
            ], 
            'diff2_idx': [
                {'txt': '北京汽车展览时间发布', 'idx': [[0, 10]]}, 
                {'txt': '', 'idx': []}, 
                {'txt': '人民日报高狄逝世', 'idx': []}
            ], 
            'list1': ['广州汽车展览', '林书豪缅怀高以翔', '人民日报高狄逝世'], 
            'list2': ['北京汽车展览时间发布', '人民日报高狄逝世'], 
            'diff_score': 0.6666666666666666
        }
```