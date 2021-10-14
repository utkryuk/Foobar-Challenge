
dp = [[None for i in range(205)] for i in range(205)]

def stair(prevhighest, left):
    if left == 0:
        return 1
    if dp[prevhighest][left]:
        return dp[prevhighest][left]
    ans = 0 
    for i in range(prevhighest+1,left+1):
        ans += stair(i , left - i)
    dp[prevhighest][left] = ans
    return ans

def solution(n):
    return stair(0,n) - 1


n = 200
print(solution(n))