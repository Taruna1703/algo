#Given the height of buildings each having width 1 , find the total rain water trapped on btw the buildings
def solve(n,arr):
	left=[0]*n
	right=[0]*n
	water=0
	if n<2:
		return 0
	elif n==2:
		return min(arr)
	else:
		for i in range(1,n):
			left[i]=max(left[i-1],arr[i-1])
		for i in range(n-2,-1,-1):
			right[i]=max(right[i+1],arr[i+1])
		print(left)
		print(right)
		for i in range(1,n-1):
			if min(left[i],right[i])-arr[i]>0:
				water=water+(min(left[i],right[i])-arr[i])
	return water
print(solve(11,[1,0,2,1,0,1,3,2,1,2,1]))
#Time Complexity O(n)
#Space Complexity O(n)