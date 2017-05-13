#coding=utf-8

def createDataSet():
    # 每一条记录以一个列表记录
    DataSet =[[1,1,'yes'],
              [1,1,'yes'],
              [1,0,'no'],
              [0,1,'no'],
              [0,1,'no']]
    # 数据的特征属性集合
    attrList = ['X0','X1']

    return DataSet,attrList