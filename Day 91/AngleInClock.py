
def findAngleInTime(hrs, min):
	return abs((30*(min/5-hrs))-(min/2))

print(findAngleInTime(1,15))