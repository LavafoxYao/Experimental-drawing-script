#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import re
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict, defaultdict

dict = {"delivery_prob": 9, "response_prob": 10, "overhead_ratio": 11, "latency_avg": 12, "latency_med": 13,
        "hopcount_avg": 14, "hopcount_med": 15, "buffertime_avg": 16, "buffertime_med": 17}


########################
# 文件目录
path = r"F:\One program\wywork\the-one-1.6.0\reports"
#path = r"F:\One平台\reports\921添加相似度不加ACK"
# 画图的纵坐标与横坐标的名称
COLNAME = "delivery_prob"
ROWNAME = "Buffsize"
# 比较指标 ==>比如 deliver_prob
norm = dict["delivery_prob"]
##########################


def getfilename():
    # 获得目录下所有的文件名
    allfiles = os.listdir(path)
    # os.path.getmtime() 函数是获取文件最后修改时间
    #allfiles = sorted(allfiles, key=lambda x: os.path.getmtime(os.path.join(path, x)))
    files = []
    for file in allfiles:
        if file.endswith(r".txt"):
            files.append(file)
    return files


def getalgoname():
    files = getfilename()
    # 将算法的名称存储到algo_name中
    algo_name = set()
    for f in files:
        #algo_name.add(re.search(r'^([A-Z]*[a-z]*){2}', f).group())
        algo_name.add(re.search(r'\d{1,5}', f).group())
        #print(algo_name);
    return algo_name


def getdata():
    # algodict = dict{}
    global target
    files = getfilename()
    algomap = {}
    for file in files:
        # 打开文件
        f = open(path + "\\" + file)
        # 正则匹配 截取符合下列规则的字符串
        # 截取数字之前的字符串
        name = re.search(r'([A-Z]*[a-z]*){3}', file).group()
        # 截取文件名中的浮点数
        para = re.search(r'[0-9]*\.?[0-9]+', file).group()
        read_buf = []
        # 读取文件中所有的数据
        for r in f:
            read_buf.append(r)
        # 如果读取的文件是空的就continue
        if len(read_buf) <= 1:
            continue
        # 读取list中的数据,并且用split分割一次(2部分)并且取第二个元素
        str = read_buf[norm].split(':', 1)[1]
        # 并将其分割成只含数字字符串的list
        target = (str.replace("\n", "").replace("\r", "").replace(" ", ""))
        # 当name不存在algomap中就新建一个{} 去存储 para 和 target
        if name not in algomap.keys():
            algomap[name] = {}
        # 这里相当于dict{"":{}}
        algomap[name][float(para)] = target
    return algomap

def painting():
    algomap = getdata()
    # 折线的颜色
    color = ["#F4606C", "#7B68EE", "#40E0D0", "#F4A460", "#B5495B", "#BEEDC7", "#D1BA74","#FB966E", "#FFC408"]
    #折线的形状
    marker = [r"-o", r"-*", r"-^", r"-v", r"-D", r"+",  r"x", r"<", r">"]
    # 图的名称
    plt.figure('DTN experimental data fig')
    ax = plt.gca()
    # 设置x轴、y轴名称
    ax.set_xlabel(ROWNAME)
    ax.set_ylabel(COLNAME)
    cnt = 0
    for key in algomap:
        x_list = []
        y_list = []
        for k in sorted(algomap[key]):
            x_list.append(str(k))
            y_list.append(algomap[key][k])
        print(x_list)
        print(y_list)
        x_list = list(map(float, x_list))
        y_list = list(map(float, y_list))
        # 画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
        # 参数c指定连线的颜色，linewidth 指定连线宽度，alpha指定连线的透明度
        ax.plot(x_list, y_list, marker[cnt], label=key, color=color[cnt], linestyle='-', linewidth=2, alpha=0.9)
        cnt += 1
    plt.legend()
    plt.show()


if __name__ == '__main__':
    painting()
