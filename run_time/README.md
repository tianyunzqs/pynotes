# 计算函数运行时间
利用装饰器，计算函数执行时间<br/>
```python
@cal_run_time
def fun():
    time.sleep(5)
```
```python
[out]: fun cost 5000 ms
```