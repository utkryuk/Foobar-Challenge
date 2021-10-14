import math

g = 0
def gcd(x, y):
    global g
    if y==0:
        return x
    g+=(x - x%y)//y
    return gcd(y,x%y)

def solution(x, y):
    x = int(x)
    y = int(y)
    ans = gcd(x,y)
    if ans != 1:
        return "impossible"
    return str(g-1)

x = '2'
y = '1'
print(solution(x,y))    