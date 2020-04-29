import sys
sys.stdin = open("..//input.txt","r")
sys.stdout = open("..//output.txt","w")
# t = int(input())
# for inputing array: arr = [int(x) for x in raw_input().split()]
# 	a, b, c, x = map(int, raw_input().split())


def computexor(n):
	val = n%4
	if val == 0:
		return n
	elif val == 1:
		return 1
	elif val == 2:
		return n + 1
	else:
		return 0

def solution(start, length):
    if length == 1:
        return start
    ans = computexor(start + 2*(length-1))
    if start > 1:
        ans = ans^computexor(start - 1)
    for i in range(length-2):
        a = length - 2 - i
        b = start + length*(2 + i) - 1
        ans = ans^computexor(a+b)^computexor(b)
    return ans

start, length = map(int, raw_input().split())
print(solution(start,length))