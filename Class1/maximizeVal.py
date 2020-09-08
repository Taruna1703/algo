#Given an unsorted array, find the 
#Max |A[i]-A[j]|+|i-j| where i!=j
def solve(n,arr):
	arr1=[0]*n
	arr2=[0]*n
	for i in range(n):
		arr1[i]=arr[i]+i
		arr2[i]=arr[i]-i
	max1=arr1[0]
	min1=arr1[0]
	max2=arr2[0]
	min2=arr2[0]
	#print(arr1)
	#print(arr2)
	for i in range(n):
		if arr1[i]>max1:
			max1=arr1[i]
		if arr2[i]>max2:
			max2=arr2[i]
		if arr1[i]<min1:
			min1=arr1[i]
		if arr2[i]<min2:
			min2=arr2[i]
	return max(max1-min1,max2-min2)
print(solve(10,[10,3,9,17,12,16,21,2,14,25]))

#Time Complexity O(n)
#Space Complexity O(n)