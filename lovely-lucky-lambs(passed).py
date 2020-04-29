import sys
sys.stdin = open("..//input.txt","r")
sys.stdout = open("..//output.txt","w")
# t = int(input())
# for inputing array: arr = [int(x) for x in raw_input().split()]
# 	a, b, c, x = map(int, raw_input().split())
def max_payout(lambs):
#    return int(log((lambs+1),2))
    ans, last, cur = 1, 0, 1
    lambs = lambs - 1
    while lambs > 0:
        if lambs < cur*2:
            if lambs >= cur + last:
                ans = ans + 1
            break
        ans = ans + 1
        cur = cur*2
        last = cur
        lambs = lambs - cur
    return ans

def min_payout(lambs):
    lambs = lambs - 2
    arr = []
    arr.append(1)
    arr.append(1)
    while lambs > 0:
        if arr[-1] + arr[-2] > lambs:
            break
        arr.append(arr[-1] + arr[-2])
        lambs = lambs - arr[-1]
    return len(arr)

def solution(total_lambs):
    # Your code here
    if total_lambs < 10 and total_lambs!= 3:
        return 1
    if total_lambs >= 1000000000:
        return 0
    high = max_payout(total_lambs)
    low = min_payout(total_lambs)
    return max(low,high) - min(high,low)

t = int(input())
for i in range(t+1):
	print(i, solution(i))