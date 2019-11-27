# -*- coding: utf-8 -*-
# @Time        : 2019/11/27 10:23
# @Author      : tianyunzqs
# @Description : pandas读写Excel文件

import pandas as pd

# 读取excel
data = pd.read_excel(r'example.xlsx', sheet_name='Sheet1')
# 去除“序号”
data = data[['姓名', '性别', '年龄', '身高', '体重']]
# 或者如下语句也可去除“序号”
data2 = data.filter(items=['姓名', '性别', '年龄', '身高', '体重'])
print(data)
print(data2)

# 选择“性别为男”的行
data = data[data['性别'].apply(lambda x: x == '男')]
print(data)

# 以行遍历
for index, row in data.iterrows():
    print('姓名：{0}，性别：{1}'.format(row['姓名'], row['性别']))


# 写excel
write_data = []
for index, row in data.iterrows():
    write_data.append([row['姓名'], row['性别'], '是' if int(row['年龄']) > 25 else '否'])

# 标题
columns = ['姓名', '性别', '是否大于25岁']
# 转换为DataFrame格式
df = pd.DataFrame(write_data, columns=columns)
# 写入Excel文件
with pd.ExcelWriter('example2.xlsx') as writer:
    df.to_excel(writer, index=False, sheet_name='pandas create')
