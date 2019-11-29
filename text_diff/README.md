# 文本差异性比较
利用python自带的difflib包，比较两文本之间的差异<br/>
```python
[in1]: 中国的首都是北京
[in2]: 北京是中国的首都
[out]: {
            'is_same': False, 
            'diff1_idx': [[5, 8]],  # 左开右闭区间 
            'diff2_idx': [[0, 3]],  # 左开右闭区间
            'string1': '中国的首都是北京', 
            'string2': '北京是中国的首都', 
            'sim_score': 0.625  # 两个输入字符串的相似度
        }
```
