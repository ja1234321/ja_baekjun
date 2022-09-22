def sum_value(v):
    if v <= N:
        if tree[v]:
            return tree[v]
        a = sum_value(2*v)
        b = sum_value(2*v+1)
        return a + b
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split())
    tree = [0] * (N + 1)
    for _ in range(M): # 리프 노드의 데이터를 받는다.
        a, b = map(int, input().split()) # 리프 노드의 인덱스, 데이터
        tree[a] = b
    # c = [0, 1,2,3,4,5]
    '''
    값을 저장하는거랑 다르게 하기...'''
    # tree = [0, 0, 0, 3, 1, 2]
    c = [0] * (N + 1)
    for i in range(1, N+1):
        c[i] = i
    print(f'#{tc} {sum_value(L)}')
    # print(tree[L])