def solution(map):
    r = len(map)
    c = len(map[0])
    ans = [[[0,0] for i in range(c)] for i in range(r)]
    for i in range(r):
        for j in range(c):
            code = map[i][j]
            if i>0 and j>0:
                if code == 0:
                    ans[i][j][0] = min(ans[i][j-1][0], ans[i-1][j][0]) + 1
                    ans[i][j][1] = min(ans[i][j-1][1], ans[i-1][j][1]) + 1
                elif code == 1:
                    ans[i][j][0] = 1000000000
                    ans[i][j][1] = min(ans[i][j-1][0],ans[i-1][j][0]) + 1
            elif i>0:
                if code == 0:
                    ans[i][j][0] = ans[i-1][j][0] + 1
                    ans[i][j][1] = ans[i-1][j][1] + 1
                elif code == 1:
                    ans[i][j][0] = 1000000000
                    ans[i][j][1] = ans[i-1][j][0] + 1
            elif j>0:
                if code == 0:
                    ans[i][j][0] = ans[i][j-1][0] + 1
                    ans[i][j][1] = ans[i][j-1][1] + 1
                elif code == 1:
                    ans[i][j][0] = 1000000000
                    ans[i][j][1] = ans[i][j-1][0] + 1
            elif i==0 and j==0:
                if code == 0:
                    ans[i][j][0] = ans[i][j][1] = 1
                elif code == 1:
                    ans[i][j][0] = 1000000000
                    ans[i][j][1] = 1

    # assert min(ans[r-1][c-1][0],ans[r-1][c-1][1]) < 100000000
    return min(ans[r-1][c-1][0],ans[r-1][c-1][1])

map = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]]
import numpy as np 
print(np.matrix(map))
print(solution(map))