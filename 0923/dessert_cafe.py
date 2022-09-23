# d완전 탐색에서 가장 중요한건, 현재 할 수 있는 건 모두 해보겠다는 게, 완전 탐색의 기본 마인드이다.
# 내가 할 수 있는 건 우츨 하단으로 가거나, 좌측 하단으로 가는 방법을 보기
# 좌측 하단으로 가거나, 좌측 상단으로 가는것이 가능하다...
# 우측 상단으로가는경우는 직진방향 밖에 없다...
dr = [1,1,-1,-1]
dc = [1,-1,-1,1]


def dfs(r,c, dir, visited): #시작위치, 방향, 방문한 곳의 정보
    global max_value
    # 1진행: 2경우: 직진이거나 다음방향으로 이동하기
    # 1 - 1) 직진
    if visited and (r, c) == (i, j):
        # 2. 종료 상황이니까, 반환하기 . 비어있는 visited면, 돌아온것임
        if max_value < len(visited):
            max_value = len(visited)
        # 7. 투어 완료인 상황, 디저트 먹은 상황
        return

    # 3. 방문했던 곳이면 끝, return을 해주기
    if data[r][c] in visited:
        return
    # 6. 정상범위 이외의 장소는 끝 >> return 하기
    if r < 0 or r >= N or c < 0 or c>=N:
        return
    # 4. 방문하지 않은 곳이니까 여기서 visited하기 - 5로 가기
    visited.add(data[r][c])



    dfs(r+dr[dir], c+dc[dir], dir, visited)
    if dir < 3:
        # 1 - 2) 방향전환, dir3에서 하는 일은 제 자리로 오는 것 뿐, 방향 전환하지 않도록 하기
        dfs(r+dr[dir+1], c+dc[dir+1], dir+1, visited)

    # 5. 할 수 있는 경우를 해보고, 삭제한다.
    visited.remove(data[r][c])







T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_value = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, set())
    print(f'#{tc} {max_value if max_value < 0  else -1}')