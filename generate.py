# coding:utf-8
# @Time:2022/4/3 17:14
# @File:generate.py
import random


def init(is_num, is_low, is_up, is_sp):
    if not (is_num | is_low | is_up | is_sp):
        return [['1'], ['1'], ['1'], ['1']]

    table = [[0 for _ in range(26)] for _ in range(4)]
    # 数字
    temp = []
    if is_num:
        temp = ['0' for _ in range(10)]
        for i in range(0, 10):
            temp[i] = str(i)
    table[0] = temp

    # 小写字母
    if is_low:
        for i in range(0, 26):
            table[1][i] = chr(ord('a') + i)
    else:
        table[1] = []

    # 大写字母
    if is_up:
        for i in range(0, 26):
            table[2][i] = chr(ord('A') + i)
    else:
        table[2] = []

    # 特殊字符
    temp = []
    if is_sp:
        temp = ['0' for _ in range(32)]
        iterator = 0
        for i in range(33, 48):
            temp[iterator] = chr(i)
            iterator += 1
        for i in range(58, 65):
            temp[iterator] = chr(i)
            iterator += 1
        for i in range(91, 97):
            temp[iterator] = chr(i)
            iterator += 1
        for i in range(123, 127):
            temp[iterator] = chr(i)
            iterator += 1
    table[3] = temp
    return table


def generate(length, table):
    result = ['' for _ in range(length)]
    for i in range(length):
        result[i] = random_char(table)
    return result


def random_char(table):
    table_len = [len(table[0]), len(table[1]), len(table[2]), len(table[3])]
    total = table_len[0] + table_len[1] + table_len[2] + table_len[3]
    rand_num = random.randint(0, total)

    picked_type = table[0]
    depth = 0
    index = 0
    while rand_num > 0:
        index = rand_num
        picked_type = table[depth]
        rand_num = rand_num - table_len[depth]
        depth = depth + 1
    result = picked_type[index - 1]
    return result
