# python日志记录工具
基于python自带logging库，实现日志记录工具。该工具可配置日志保存路径、日志输出格式、日志滚动、滚动周期、保存日志副本数等相关功能<br/>
如：按天滚动，每天保存一个副本，最多保存30个副本。也即每天输出一个日志文件，当保存的日志超过副本数时，删除时间最早的日志文件<br/>

```python
# interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
# S 秒
# M 分
# H 小时
# D 天
# W 每星期（interval==0时代表星期一）
# midnight 每天凌晨
th = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                               when='D',
                                               interval=1,
                                               backupCount=30,
                                               encoding='utf-8'
                                               )
```