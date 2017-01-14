#-*- coding:utf-8 -*-
import numpy as np  

#sigmoid函数
def sigmoid(inX):
	return 1.0 / (1+exp(-inX))


#梯度下降法定参
def gradAscent(dataArray,labelArray,alpha,epochs):
	dataMat = mat(dataArray)
	labelMat = mat(labelArray)
	m,n = shape(dataMat)
	weight = ones((n,1))

	for i in range(epochs):
		h = sigmoid(dataMat*weigh)
		error = labelMat - h
		weight = weigh+alpha*dataMat.transpose()*error

	return weight


#预测
def classify(testdir,weight):
	dataArray,labelArray = loadData(testdir)
	dataMat = mat(dataArray)
	labelMat = mat(labelArray)
	h = sigmoid(dataMat*weight)
	m = len(h)
	error = 0.0

	for i in range(m):
		if int(h[i]) > 0.5:
			print int(labelMat[i]),'is classified as: 1'
			if int(labelMat[i]) != 1:
				error += 1
				print 'error'

		else:
			print int(labelMat[i]),'is classified as: 0'
			if int(labelMat[i]) != 0:
				error += 1
				print 'error'
	print 'error rate is:','%.4f' %(erorr/m)
	
	
