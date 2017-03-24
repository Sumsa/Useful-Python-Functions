def lawnmower(start,stop,flipat):
	'''
	the lawnmower function runs lanes just like mowing a lawn,
	returns an array from start to stop flipping order at flipat
	e.g lawnmower(0,10,3)
	'''
	flip=False
	order=[]
	for i in range(start,stop):
		if i%flipat==0 and i>0:
			if flip==False:
				flip=True
			else: 
				flip=False
		if flip==True:
			if i%flipat==0:
				goal=(i+flipat)
				startingpoint=i-1
			j=goal-(i-startingpoint)
		else:
			j=i
		order.append(j)
	return order
	
print lawnmower(0,50,3)


