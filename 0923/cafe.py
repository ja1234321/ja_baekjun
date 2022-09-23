
#시계방향 우측하단부터 시작: 시계방향으로 고정 3번만 돌고 자기 자신으로 돌아오기로 하세용
dc = [1,-1,-1,1]
dr = [1,1,-1,-1]
#
def dfs(r,c,dir,visited):
    global max_value
    if r < 0 or r >= N or c < 0 or c >= N:
        return
    if visited and (r,c) == (i,j) and dir == 3: # dir=3일때가 들어와야한다!
        if max_value < len(visited):
            # print(visited)
            max_value = len(visited)
        return
    if data[r][c] in visited:
        return
    visited.append(data[r][c])              # 정보 넣고
    dfs(r+dr[dir],c+dc[dir],dir,visited)
    if dir < 3:                             # 돌아오는 경우에만 도달해야하므로
        dfs(r + dr[dir + 1], c + dc[dir + 1], dir + 1, visited)
    visited.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    # 시계 방향으로 고정
    max_value = 0
    for i in range(N):
        for j in range(N):
            dfs(i,j,0,[])
    print(f'#{tc} {max_value}')