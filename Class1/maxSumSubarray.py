'''
Max Sum Contiguous Subarray
Find the contiguous subarray within an array, A of length N which has the largest sum.
'''
def solve(n,arr):
	prefixSum=[0]*n
	prefixSum[0]=arr[0]
	maxSum=arr[0]
	min_sum=arr[0]
	total=sum(arr)
	for i in range(1,n):
		prefixSum[i]=prefixSum[i-1]+arr[i]
	for i in range(n):
		maxSum=max(prefixSum[i]-min_sum,maxSum)
		min_sum=min(min_sum,prefixSum[i])
	return maxSum
print(solve(8,[-2, -5, 6, -2, -3, 1, 5, -6]))

