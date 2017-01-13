import numpy as np

class ID3:

    def __init__(self):
        self.tree = None


    def calEntropy(self,y):
        num = y.shape[0]
        labelCounts = {}
        for label in y:
            if label not in labelCounts.keys():
                labelCounts[label] = 0
            labelCounts[label] += 1

        entropy = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key]) / num
            entropy -= prob * np.log2(prob)

        return entropy


    def splitDataset(self,X,y,index,value):
        ret = []
        featVec = X[:,index]
        X = X[:,[i for i in range(X.shape[1]) if i != index]]
        for i in range(len(featVec)):
            if featVec[i]==value:
                ret.append(i)

        return X[ret,:],y[ret]


    def chooseBestFeatureToSplit(self,X,y):
        numFeatures = X.shape[1]
        oldEntropy = self.calEntropy(y)
        bestInfoGain = 0.0
        bestFeatureIndex = -1

        for i in range(numFeatures):
            featList = X[:,i]
            uniqueVals = set(featList)
            newEntropy = 0.0

            for value in uniqueVals:
                sub_X,sub_y = self.splitDataset(X,y,i,value)
                prob = len(sub_y) / float(len(y))
                newEntropy += prob * self.calEntropy(sub_y)

            infoGain = oldEntropy - newEntropy
            if infoGain > bestInfoGain:
                bestInfoGain = infoGain
                bestFeatureIndex = i

        return bestFeatureIndex


    def majorityCnt(self,labelList):
        labelCount = {}
        for vote in labelList:
            if vote not in labelCount.keys():
                labelCount[vote] = 0
            labelCount[vote] += 1
        sortedClassCount = sorted(labelCount.iteritems(),key = lambda x: x[1],reverse=True)

        return sortedClassCount[0][0]


    def createTree(self,X,y,featureIndex):
        labelList = list(y)
        if labelList.count(labelList[0]) == len(labelList):
            return labelList[0]
        if len(featureIndex) == 0:
            return self.majorityCnt(labelList)

        bestFeatIndex = self.chooseBestFeatureToSplit(X,y)
        bestFeatStr = featureIndex[bestFeatIndex]
        featureIndex = list(featureIndex)
        featureIndex.remove(bestFeatStr)
        featureIndex = tuple(featureIndex)

        myTree = {bestFeatStr:{}}
        featValues = X[:,bestFeatIndex]
        uniqueVals = set(featValues)

        for value in uniqueVals:
            sub_X,sub_y = self.splitDataset(X,y,bestFeatIndex,value)
            myTree[bestFeatStr][value] = self.createTree(sub_X,sub_y,featureIndex)

        return myTree


    def fit(self,X,y):
        if isinstance(X,np.ndarray) and isinstance(y,np.ndarray):
            pass
        else:
            try:
                X = np.array(X)
                y = np.array(y)
            except:
                raise TypeError("numpy.ndarray required for X,y")

        featureIndex = tuple(['x'+str(i) for i in range(X.shape[1])])
        self.tree = self.createTree(X,y,featureIndex)
        return self


    def predict(self,X):
        if self.tree == None:
            raise NotImplementedError("Estimator not fitted,call 'fit' first")

        if isinstance(X,np.ndarray):
            pass
        else:
            try:
                X = np.array(X)
            except:
                raise TypeError("numpy.ndarray required for X")

        def classify(tree,sample):
            featIndex = tree.keys()[0]
            secondDict = tree[featIndex]
            key = sample[int(featIndex[1:])]
            valueOfkey = secondDict[key]

            if isinstance(valueOfkey,dict):
                label = classify(valueOfkey,sample)
            else:
                label = valueOfkey
            return label


        if len(X.shape)==1:
            return classify(self.tree,X)
        else:
            results = []
            for i in range(X.shape[0]):
                results.append(classify(self.tree,X[i]))
            return np.array(results)

























