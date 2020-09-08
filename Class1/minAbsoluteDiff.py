#Given an unsorted array, find the min absolute difference btw any 2 element of array where i!=j
#Find min |A[i]-A[j]| where i!=j
def solve(arr):
	arr.sort()
	n=len(arr)
	minimum=arr[-1]
	for i in range(n-1):
		if abs(arr[i]-arr[i+1])<minimum:
			minimum=abs(arr[i]-arr[i+1])
	return minimum

print(solve([4,10,22,9,3,12,11,16]))

#Time Complexity O(nlogn)