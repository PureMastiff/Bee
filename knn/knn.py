# coding=utf-8


from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 2.0], [1.2, 0.1], [0.1, 1.4], [0.3, 3.5]])
    labels = ['A', 'B', 'C', 'D']
    return group, labels


def classify(input, dataSet, label, k):
    dataSize = dataSet.shape[0]
    print dataSize
    print tile(input, (dataSize,1))
    diff = tile(input, (dataSize,1)) - dataSet
    print 'diff:{}'.format(diff)
    sqdiff = diff ** 2
    print sqdiff

    squareDist = sum(sqdiff, axis=1)
    print squareDist
    dist = squareDist ** 0.5
    print dist
    sortedDistIndex = argsort(dist)  # 返回的是从小到大的索引值

    print sortedDistIndex

    classCount = {}
    for i in range(k):

        voteLabel = label[sortedDistIndex[i]]
        print voteLabel
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
        print classCount

    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes

dataset, lables = createDataSet()

input = array([1.1, 0.3])
k = 4
output = classify(input, dataset, lables, k)
print output