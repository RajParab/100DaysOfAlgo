

def sameBST(bst1, bst2):
	if len(bst1)==0 and len(bst2)==0:
		return True
	if len(bst1)!= len(bst2) or bst1[0]!=bst2[0]:
		return False
	

	leftSubtree1=getLeftSubtree(bst1)
	rightSubtree1=getRightSubtree(bst1)
	leftSubtree2=getLeftSubtree(bst2)
	rightSubtree2=getRightSubtree(bst2)
	return sameBST(leftSubtree1, leftSubtree2) and sameBST(rightSubtree1,rightSubtree2)

def getLeftSubtree(bst):
	leftSubtree=[]
	for i in bst[1:]:
		if i < bst[0]:
			leftSubtree.append(i)
	return leftSubtree

def getRightSubtree(bst):
	rightSubtree=[]
	for i in bst[1:]:
		if i >= bst[0]:
			rightSubtree.append(i)
	return rightSubtree
print(sameBST([10,15,8,12,94,81,5,2,11],[10,8,5,15,2,11,12,94,81]))