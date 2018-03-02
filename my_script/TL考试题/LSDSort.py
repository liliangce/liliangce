# /usr/bin/evn python
# coding:utf-8
import copy

SAMPLE = [1, 2, 43, 65, 7, 897, 43, 2, 67, 87, 23, 34, 2]


class LSDSort(object):
    """
    基数排序算法：从个位数开始排序，只取个位数排序，不管其他位数

    """
    def __init__(self):
        self.temp = copy.copy(SAMPLE)

    def lsd_sort(self):
        len_temp = len(self.temp)
        for i in range(1, len_temp):
            pass

