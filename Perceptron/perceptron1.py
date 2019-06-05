# -*- coding:utf-8 -*-
"""
感知机（李航---统计学习方法）

内容：原始感知机实现

date: 2019/05/27
"""
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt


def sign(v):
    if v >= 0:
        return 1
    else:
        return -1


def train(train_num, train_datas, lr):
    w = [0, 0]
    b = 0
    for i in range(train_num):
        x = random.choice(train_datas)      # 参数选择
        x1, x2, y = x
        if (y*sign(w[0]*x1+w[1]*x2+b))<=0:
            w[0] += lr*y*x1
            w[1] += lr*y*x2
            b += lr*y
    return w,b


def plot_points(train_datas, w, b):
    plt.figure()
    x1 = np.linspace(0, 8, 100)
    x2 = (-b-w[0]*x1)/w[1]
    plt.plot(x1,x2, color='r', label='y1 data')
    datas_len = len(train_datas)
    for i in range(datas_len):
        if (train_datas[i][-1] == 1):
            plt.scatter(train_datas[i][0], train_datas[i][1], s=50)
        else:
            plt.scatter(train_datas[i][0], train_datas[i][1], marker='x' ,s=50)
    plt.show()


if __name__=='__main__':
    train_data1 = [[1, 3, 1], [2, 2, 1], [3, 8, 1], [2, 6, 1]]  # 正样本
    train_data2 = [[2, 1, -1], [4, 1, -1], [6, 2, -1], [7, 3, -1]]  # 负样本
    train_datas = train_data1 + train_data2  # 样本集
    w, b = train(train_num=50, train_datas=train_datas, lr=0.01)
    plot_points(train_datas, w, b)