from ID3 import id3

if __name__ == '__main__':
	X = [[0, 1, 1, 0, 1],
		[1, 2, 0, 1, 0],
		[1, 0, 0, 0, 1],
		[1, 1, 0, 1, 1],
		[2, 1, 1, 0, 1]]
	y = ['yes','yes','no','no','no']
  
	clf = id3()
	clf.fit(X,y)
  
	print clf.predict(X)
