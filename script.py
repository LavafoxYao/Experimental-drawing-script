#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import re
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict, defaultdict
from pylab import mpl

# 指定默认字体
# 如果需要在图中输出中文选择将下面的 mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 注释放开
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# mpl.rcParams['font.sans-serif'] = ['Consolas']
# 解决保存图像是负号'-'显示为方块的问题
mpl.rcParams['axes.unicode_minus'] = False

dict = {"delivery_prob": 9, "response_prob": 10, "overhead_ratio": 11, "latency_avg": 12, "latency_med": 13,
        "hopcount_avg": 14, "hopcount_med": 15, "buffertime_avg": 16, "buffertime_med": 17}


########################
# 文件目录
path = r"E:\论文相关\计算机学报\最终reports\buffsize"
#path = r"F:\One平台\reports\921添加相似度不加ACK"
# 画图的纵坐标与横坐标的名称
COLNAME = "平均时延(S)"
ROWNAME = "缓存大小(MB)"
# 比较指标 ==>比如 deliver_prob
norm = dict["latency_avg"]
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
        name = re.search(r'([A-Z]*[a-z]*-*){100}', file).group()
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
    color = ["#7B68EE", "#40E0D0", "#F4606C", "#F4A460", "#B5495B", "#BEEDC7", "#D1BA74", "#FB966E", "#FFC408"]
    #折线的形状
    marker = [r"-*", r"-^","-o", r"-v", r"-D", r"+",  r"x", r"<", r">"]
    # 图的名称
    plt.figure('DTN experimental data fig')
    ax = plt.gca()
    # 设置x轴、y轴名称
    ax.set_xlabel(ROWNAME)
    ax.set_ylabel(COLNAME)
    cnt = 0
    # x的界限
    x_min = sys.maxsize
    x_max = -sys.maxsize - 1
    # y轴的界限
    y_min = sys.maxsize
    y_max = -sys.maxsize - 1
    for key in algomap:
        x_list = []
        y_list = []
        for k in sorted(algomap[key]):
            x_min = min(x_min, k)
            x_max = max(x_max, k)
            y_min = min(y_min, float(algomap[key][k]))
            y_max = max(y_max, float(algomap[key][k]))
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
    # diff_x x轴的为上界和下界之间的差值
    diff_x = x_max - x_min
    dir_min_x = x_min - diff_x / 20
    dir_max_x = x_max + diff_x / 20
    # diff_y y轴的为上界和下界之间的差值
    diff_y = y_max - y_min
    dir_min_y = y_min - diff_y / 20
    dir_max_y = y_max + diff_y / 2
    # 设置X轴的范围
    plt.xlim(dir_min_x, dir_max_x)
    # 设置y轴的范围
    plt.ylim(dir_min_y, dir_max_y)
    # plt.lengend() 生成图例,为了帮助我们展示每个数据对应的图像名称
    # loc 固定图例的位置 prop 设置图例的属性
    plt.legend(loc="upper left", prop={'size': 7})
    plt.savefig(r"E:\论文相关\计算机学报\实验结果图\缓存_平均时延.png")
    plt.show()


if __name__ == '__main__':
    painting()
