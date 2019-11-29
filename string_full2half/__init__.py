# -*- coding: utf-8 -*-
# @Time        : 2019/11/29 16:59
# @Author      : tianyunzqs
# @Description : 


def string_full_to_half(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring


if __name__ == '__main__':
    s = 'ａｂｃｄｅｆwxy'
    print(string_full_to_half(s))
