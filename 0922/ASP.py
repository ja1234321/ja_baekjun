def solve(i,j):
    m = i + 1
    # if m == N:
    #     print(S)
    #     return
    while m < j and arr[m][0] < arr[i][1]:
        m += 1
    tmp = set()
    if m < j :
        print(123123)
        tmp.add(arr[m])
        tmp.update(solve(m,j))
        return tmp
    print(tmp)
    return tmp

arr = [(0,0),(1,4),(3,5),(1,6),(5,7),(3,8),(5,9),(6,10),(8,11),(2,13),(12,14)]
N = 10
# S = set()
print(solve(0,N+1))