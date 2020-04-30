import sys
sys.stdin = open("..//input.txt","r")
sys.stdout = open("..//output.txt","w")
# t = int(input())
# for inputing array: arr = [int(x) for x in raw_input().split()]
# 	a, b, c, x = map(int, raw_input().split())

def solution(n):
	if n<=4:
		return 1
	ans  = 0
	dp = [[ 0 for x in range(n+1)] for y in range(n+1)]
	dp[3][2] = 1
	dp[4][2] = 1
	for i in range(2,n+1):
		if i not in [2,3,4]:
			for j in range(2,n+1):
				if j==2:
					dp[i][2] = dp[i-2][2] + 1
				else:
					dp[i][j] = dp[i-j][j] + dp[i-j][j-1]

	for i in range(n+1):
		ans = ans + dp[n][i]
	#print(dp)
	return ans	


n = int(input())
print(solution(n))