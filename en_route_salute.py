def en_route_salute(s):
    counter, sum  = 0, 0
    for c in s:
        if c == '>':
            counter += 1
        elif c == '<':
            sum += counter
    return sum*2

def solution(s):
    print(en_route_salute(s))