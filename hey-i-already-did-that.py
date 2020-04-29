import sys
sys.stdin = open("..//input.txt","r")
sys.stdout = open("..//output.txt","w")
# t = int(input())
# for inputing array: arr = [int(x) for x in raw_input().split()]
# 	a, b, c, x = map(int, raw_input().split())

def subtract(x,y,b):
	ans = []
	for i in range(len(x)):
		if x[i] < y[i]:
			x[i] = x[i] + b
			x[i+1] = x[i+1] - 1
		ans.append(str(x[i]-y[i]))
	ans.reverse()
	return ''.join(ans)


def conv(x):
	arr = []
	for i in range(len(x)):
		temp = ord(x[i]) - 48
		arr.append(temp)
	arr.reverse()
	return arr

def s(n,b):
	x_int = ''.join(sorted(n, reverse = True))
	y_int = ''.join(sorted(n, reverse = False))
#	print(x_int, y_int)
	if len(x_int) != len(n):
		x_int = '0'*(len(n)-len(x_int)) + x_int
	if len(y_int) != len(n):
		y_int = '0'*(len(n)-len(y_int)) + y_int

	x1 = conv(x_int)
	y1 = conv(y_int)
#	print(x1,y1)
#	print(subtract(x1,y1,b))
	return subtract(x1,y1,b)

def solution(n,b):
	ans = 0
	Dict = {}
	while 1:
		temp = s(n,b)
		if Dict.get(temp) == None:
			print(temp)
			Dict[temp] = 1
			ans = ans + 1
			n = temp
		else:
			break
	return ans


n = input()
b = int(input())

print(solution(n,b))

