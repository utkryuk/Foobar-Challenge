import sys
sys.stdin = open("..//input.txt","r")
sys.stdout = open("..//output.txt","w")

def solution(n):
    n = long(n)
    ans = 0
    while(n!=1):
        if n&1 == 0:
            n = n>>1
        elif (n+1)&n > (n+1)&(n-2) or n==3:
            n = n - 1
        else:
            n = n + 1
        ans = ans + 1
    return ans

n = input()
print(solution(n))
