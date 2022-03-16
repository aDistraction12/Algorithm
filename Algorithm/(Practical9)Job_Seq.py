print("Name : Sumit Singh\nRoll No : 4354\n")

def printJobScheduling(arr, t):
	n = len(arr)
	for i in range(n):
		for j in range(n - 1 - i):
			if arr[j][2] < arr[j + 1][2]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	result = [False] * t
	job = ['-1'] * t
	for i in range(len(arr)):
		for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
			if result[j] is False:
				result[j] = True
				job[j] = arr[i][0]
				break

	print(job)
arr = [['a', 2, 150], 
	['b', 1, 49],
	['c', 2, 76],
	['d', 1, 26],
	['e', 3, 94]]
print("Following is maximum profit sequence of jobs")
printJobScheduling(arr, 3)
