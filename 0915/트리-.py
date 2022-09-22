def subtree(v):
    global cnt
    if v:
        cnt += 1
        subtree(ch1[v])
        subtree(ch2[v])

#
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    ch1 = [0] *(V + 1)
    ch2 = [0] *(V + 1)
    for i in range(E):
        if ch1[arr[2*i]]==0:
            ch1[arr[2*i]] = arr[2*i+1]
        else:
            ch2[arr[2*i]] = arr[2*i+1]
    cnt = 0
    subtree(N)
    print(f'#{tc} {cnt}')


'''
[2, 1, 2, 5, 1, 6, 5, 3, 6, 4]
3
[2, 6, 6, 4, 6, 5, 4, 1, 5, 3]
1

[7, 6, 7, 4, 6, 9, 4, 11, 9, 5, 11, 8, 5, 3, 5, 2, 8, 1, 8, 10]
3
'''