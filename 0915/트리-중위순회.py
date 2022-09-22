N = int(input())

arr = [list(input().split()) for _ in range(N)]
lst = [0]
parent = [0]*(N+1)
for i in range(N):
    lst.append(arr[i][1])
    if len(arr[i]) == 4:
        parent[int(arr[i][2])] = int(arr[i][0])
        parent[int(arr[i][3])] = int(arr[i][0])
# 노드의 부모를 값으로 한 리스트: parent
#  노드랑 데이터 넣는 곳...
for i in range(N, 2, -2):
    # 마지막 노드부터,
    if lst[parent[i]]
'''
노드 정보를 받는 곳, 
배열의 크기는 노드가 7개, 높이가 3일때, 1~15까지 가능
높이가 501개...? 2배가 되도록하기...?
저장방식을 다르게...자식번호를 두개로 부모노드를 인덱스로, 값은 정보를 넣기

'''


def postorder(v):
    # child는 연산자일수도 있기에
    if data[v].isdigit():  # v피 연산자일때는 값을 반환, 연산자일때는 왼쪽과 오른쪽 자식을 조회하고 연산까지 하기
        return float(data[v])  # 여기를 엄청 하고싶었어...
    # 왼쪽 자식 결과를 얻고
    # 오른쪽 자식 결과를 얻어서
    # 연산해서 반환
    r1 = postorder(child[0][v])
    r2 = postorder(child[1][v])
    if data[v] == "+":
        return r1 + r2
    elif data[v] == '-':
        return r1 - r2
    elif data[v] == '*':
        return r1 * r2
    elif data[v] == '/':
        return r1 / r2


for tc in range(1, 11):
    N = int(input())
    # 각 노드의 자식 노드의 정보(인덱스)가 들어가는 배열
    child = [[0]* (N + 1) for _ in range(2)]
    # 각 노드가 가지고 있는 value 를 저장하는 배열
    data = [0] *(N + 1)
    for i in range(N):
        info = input().split()
        # input 은 2개일때 피연산자, 4개일때 연산자
        if info[1].isdigit():
        # if info[1] in '+-*/':
            data[int(info[0])] = info[1]
        else:
            # 연산자일때, info에 왼쪽 자식과 오른쪽 자식이 존재..
            child[0][int(info[0])] = int(info[2])
            child[1][int(info[0])] = int(info[3])
    print(data)
    print(child)
    #
    def postorder(v):
        # child는 연산자일수도 있기에
        if data[v].isdigit():                       # v피연산자일때는 값을 반환, 연산자일때는 왼쪽과 오른쪽 자식을 조회하고 연산까지 하기
            return  float(data[v])                  # 여기를 엄청 하고싶었어...
        # 왼쪽 자식 결과를 얻고
        # 오른쪽 자식 결과를 얻어서
        # 연산해서 반환
        r1 = postorder(child[0][v])
        r2 = postorder(child[1][v])
        if data[v] == "+":
            return r1 + r2
        elif data[v] == '-':
            return r1 - r2
        elif data[v] == '*':
            return r1 * r2
        elif data[v] == '/':
            return  r1/r2
    result = postorder(1)
    print(int(result))




'''
for tc in range(1,11):
# 첫 줄에는 정점의 개수 N
    N = int(input())
# 그 다음 N 줄에 정점의 정보
# 정점이 정수면 정점 번호와 양의 정수
# 연산자이면 정점 번호, 연산자, 왼쪽, 오른쪽 자식의 정점 번호
# 정점 번호는 1부터 N까지의 정수, 루트 정점의 번호는 항상 1
    arr = [list(input().split()) for _ in range(N)]
    lst = [0]
    perent = [0]*(N+1)
    # 정점 번호별로 값을 새리스트에 저장
    for i in range(N):
        lst.append(arr[i][1])
        if len(arr[i]) == 4:
            # 자식 - 부모를 연결하는 리스트
            perent[int(arr[i][2])] = int(arr[i][0])
            perent[int(arr[i][3])] = int(arr[i][0])
    # 계산을 위한 변수
    cal = 0
    # 자식에게 연결된 부모를 계산하는 과정
    for j in range(N,2,-2):
        if lst[perent[j]] == '-':
            cal = float(lst[j-1]) - float(lst[j])
            lst[perent[j]] = cal
        elif lst[perent[j]] == '+':
            cal = float(lst[j-1]) + float(lst[j])
            lst[perent[j]] = cal
        elif lst[perent[j]] == '*':
            cal = float(lst[j-1]) * float(lst[j])
            lst[perent[j]] = cal
        elif lst[perent[j]] == '/':
            cal = float(lst[j-1]) / float(lst[j])
            lst[perent[j]] = cal
    print(f'#{tc} {int(cal)}')
    '''

def subtree(v):
    global cnt
    if ch1[v]:
        cnt += 1
        subtree(ch1[v])
    if ch2[v]:
        cnt += 1
        subtree(ch2[v])
    return



T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    arr = list(map(int, input().split()))


    for i in range(0,2*E,2):
        if not ch1[arr[i]]:
            ch1[arr[i]] = arr[i+1]
        else:
            ch2[arr[i]] = arr[i+1]
    cnt = 0
    subtree(N)
    if N in arr:
        print(f'#{tc} {cnt+1}')
    else:
        print(f'#{tc} 0')