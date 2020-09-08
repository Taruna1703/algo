'''
Given an unsorted integer array A of size N.
Find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
Return 0 if the array contains less than 2 elements.
'''

l1=[10,4,15,2,18,9,1,12]
l2=[2,4,8,11]
l3=[ 83564666, 2976674, 46591497, 24720696, 16376995, 63209921, 25486800, 49369261, 20465079, 64068560, 7453256, 14180682, 65396173, 45808477, 10172062, 28790225, 82942061, 88180229, 62446590, 77573854, 79342753, 2472968, 74250054, 17223599, 47790265, 24757250, 40512339, 24505824, 30067250, 82972321, 32482714, 76111054, 74399050, 65518880, 94248755, 76948016, 76621901, 46454881, 40376566, 13867770, 76060951, 71404732, 21608002, 26893621, 27370182, 35088766, 64827587, 67610608, 90182899, 66469061, 67277958, 92926221, 58156218, 44648845, 37817595, 46518269, 44972058, 27607545, 99404748, 39262620, 98825772, 89950732, 69937719, 78068362, 78924300, 91679939, 52530444, 71773429, 57678430, 75699274, 5835797, 74160501, 51193131, 47950620, 4572042, 85251576, 49493188, 77502342, 3244395, 51211050, 44229120, 2135351, 47258209, 77312779, 37416880, 59038338, 96069936, 20766025, 35497532, 67316276, 38312269, 38357645, 41600875, 58590177, 99257528, 99136750, 4796996, 84369137, 54237155, 64368327, 94789440, 40718847, 12226041, 80504660, 8177227, 85151842, 36165763, 72764013, 36326808, 80969323, 22947547, 76322099, 7536094, 18346503, 65759149, 45879388, 53114170, 92521723, 15492250, 42479923, 20668783, 64053151, 68778592, 3669297, 73903133, 28973293, 73195487, 64588362, 62227726, 17909010, 70683505, 86982984, 64191987, 71505285, 45949516, 28244755, 33863602, 18256044, 25110337, 23997763, 81020611, 10135495, 925679, 98158797, 73400633, 27282156, 45863518, 49288993, 52471826, 30553639, 76174500, 28828417, 41628693, 80019078, 64260962, 5577578, 50920883, 16864714, 54950300, 9267396, 56454292, 40872286, 33819401, 75369837, 6552946, 26963596, 22368984, 43723768, 39227673, 98188566, 1054037, 28292455, 18763814, 72776850, 47192134, 58393410, 14487674, 4852891, 44100801, 9755253, 37231060, 42836447, 38104756, 77865902, 67635663, 43494238, 76484257, 80555820, 8632145, 3925993, 81317956, 12645616, 23438120, 48241610, 20578077, 75133501, 46214776, 35621790, 15258257, 20145132, 32680983, 94521866, 43456056, 19341117, 29693292, 38935734, 62721977, 31340268, 91841822, 22303667, 96935307, 29160182, 61869130, 33436979, 32438444, 87945655, 43629909, 88918708, 85650550, 4201421, 11958347, 74203607, 37964292, 56174257, 20894491, 33858970, 45292153, 22249182, 77695201, 34240048, 36320401, 64890030, 81514017, 58983774, 88785054, 93832841, 12338671, 46297822, 26489779, 85959340 ]

'''
1,2,4,9,10,12,15,18
ans=5
'''
'''
def solve(arr):
	n=len(arr)
	mini=arr[0]
	maxi=arr[0]
	for i in range(n):
		if arr[i]>maxi:
			maxi=arr[i]
		if arr[i]<mini:
			mini=arr[i]

	l=[-1]*(maxi-mini+1)

	for i in range(n):
		l[arr[i]-mini]=arr[i]

	f=0
	maxDif=0

	#print(l)


	for i in range(-mini+maxi+1):
		if l[i]==-1 and f==0:
			count=1
			f=1
		elif l[i]==-1 and f==1:
			count+=1
			f=1
		elif l[i]!=-1:
			f=0
			count=0
		if count>maxDif:
			maxDif=count
	return maxDif+1
print(solve(l2))

#Time Complexity O(n)
#Space Complexity O(maximum-minimum+1 i.e range of numbers)

'''
def maximumGap( A):
    arr=A
    n=len(arr)
    if n<2:return 0
    mini=arr[0]
    maxi=arr[0]
    for i in range(n):
    	if arr[i]>maxi:
    		maxi=arr[i]
    	if arr[i]<mini:
    		mini=arr[i]
    gap=(maxi-mini)/(n-1)
    if gap==0:return 0
    Min=mini-1
    Max=maxi+1
    buckets=[[Min,Max] for i in range(n)]
    for i in A:
    	position=int((i-mini)/gap)
    	buckets[position][0]=max(buckets[position][0],i)
    	buckets[position][1]=min(buckets[position][1],i)
    ans=0
    previous=buckets[0][1]
    for i in range(n):
    	if buckets[i][0]==Min and buckets[i][1]==Max:
    		continue
    	ans=max(ans,buckets[i][1]-previous)
    	previous=buckets[i][0]
    return ans

print(maximumGap(l3))
 






