#coding=utf-8

from math import log

#计算给定数据的香农熵
def calcShannonEnt(dataSet):
    num_sample = len(dataSet)
    labelCounts = {}
    for record in dataSet:
        Ci = record[-1] #获得标签
        labelCounts[Ci]=labelCounts.get(Ci,0)+1

    #计算香农熵
    shannonEnt = 0.0
    for key in labelCounts:
        # 计算Pi
        prob = float(labelCounts[key])/num_sample
        shannonEnt -=prob*log(prob,2)
    return shannonEnt

# 划分数据集,dataSet：待划分数据集，axis：表示按dataSet[axis]列划分,value：划分值
# 其实也就是在dataSet中，取出dataSet[axis]列中值等于value的这一行数据
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for record in dataSet:
        if record[axis] ==value:
            # 思路：取出0～axis和sxix+1～结尾的数据，然后合并
            reducedFeatVec = record[:axis]
            reducedFeatVec.extend(record[axis+1:])
            retDataSet.append(reducedFeatVec)
    # 返回子集数据
    return retDataSet


# 从所有attrList中选择最佳的分裂属性
def chooseBestFeatureToSplit_ID3(dataSet,attrList):
    numFeature = len(dataSet[0])-1
    # 计算数据集的信息熵H(D)
    baseEntropy = calcShannonEnt(dataSet)

    bestInfoGain = 0
    bestFeature_index = -1

    # 对每一个特征都计算信息增益，取信息增益最大的特征
    for i in range(numFeature):
        # 第i个特征都有哪些取值
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)

        # newEntropy=H(D)
        newEntropy = 0.0
        # 计算每一个特征A对数据集D的经验条件熵H(D|A)=|D1|/|D|*H(D1)+|D2|/|D|*H(D2)+...+|Dn|/|D|*H(Dn)
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            # 计算的是|Di|/|D|
            prob = len(subDataSet)/float(len(dataSet))
            # prob * calcShannonEnt(subDataSet)=|Di|/|D|*H(Di)
            newEntropy +=prob * calcShannonEnt(subDataSet)

        # 计算该特征的信息增益
        infoGain = baseEntropy- newEntropy

        # 求最佳分裂点，infoGain最大的特征
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature_index = i

    return attrList[bestFeature_index]