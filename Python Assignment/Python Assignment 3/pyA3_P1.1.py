import numpy as np

lis = [2,4,5,6,8,3,9,4,6,8]

func = np.log()


def myReduce(func, lis):
    oList = [func(i) for i in lis]
    return oList


