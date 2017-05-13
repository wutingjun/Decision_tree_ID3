#coding=utf-8

import loadData
import feature_split

# 返回属性值(类别出现次数)个数最多的类型
def majorityCnt(classList):
    classCount = {}
    for Ci in classList:
        classCount[Ci]=classCount.get(Ci,0)+1

    # 按value值降序排列
    sortedClassCount = sorted(classCount.items(),key=lambda e:e[1],reverse=True)
    return sortedClassCount[0][0]

 #创建树的函数代码
def createTree(dataSet,attrList):
    # 创建根节点myTree
    myTree={}

    # 判断所有类别是否是同一类别
    classList = [example[-1]  for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]

    # 判断属性集是否为空
    if len(attrList) ==0:
        return majorityCnt(classList)   #遍历完所有特征值时返回出现次数最多的

    # 从所有attrList中选择最佳的分裂属性
    best_split_feat =feature_split.chooseBestFeatureToSplit_ID3(dataSet,attrList)
    # best_split_feat特征对应的下标
    best_split_feat_index=attrList.index(best_split_feat)

    # 计算subattrList <- attrList-best_split_feat,subattrList是attrList的子集
    del(attrList[best_split_feat_index])
    subattrList=attrList[:]

    # best_split_feat的特征都有哪些取值
    featValues = [example[best_split_feat_index] for example in dataSet]
    uniqueVals = set(featValues)

    myTree[best_split_feat]={}
    for value in uniqueVals:
        # 按照属性best_split_feat所有不同值Vi，将Dataset分为不同的子集Di，对于每一个做进行递归建树
        Di=feature_split.splitDataSet(dataSet,best_split_feat_index,value)
        # value有多个取值就有多个子树
        myTree[best_split_feat][value]=createTree(Di,subattrList)
    return myTree

if __name__=="__main__":
    DataSet,attrList = loadData.createDataSet()
    print createTree(DataSet,attrList)