print('--------------babyjin')
def f(i,k):
    global ans
    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] and card[1]== card[2]:
            tri += 1
        if card[0]+ 1 == card[1] and card[1]+1== card[2]:
            run += 1
        if card[3] == card[4] and card[4]== card[5]:
            tri += 1
        if card[3]+ 1 == card[4] and card[4]+1== card[5]:
            run += 1
        if tri+run == 2:
            ans = 'Baby Gin'


    else:
        for j in range(i,k):
            card[i], card[j] = card[j], card[i]
            f(i+1,k)
            card[i], card[j] = card[j], card[i]


card=list(map(int,input()))
ans= 'lose'
f(0,6)
#
def f(i, k):

    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
            run += 1
        if card[3] == card[4] and card[4] == card[5]:
            tri += 1
        if card[3] + 1 == card[4] and card[4] + 1 == card[5]:
            run += 1
        if tri + run == 2:
            return 1
        else:
            return 0


    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            if f(i + 1, k):
               return 1
            card[i], card[j] = card[j], card[i]
        return 0


card = list(map(int, input()))
ans = 'lose'
ans = f(0, 6)
if ans:
    print(f'#{tc} Baby Gin')
else:
    print(f'#{tc} Lose')


print('--------------------과제: 최대상금')
                                                                # 1문자열은 자리바꿀수없으니까, 배열합을 구할게 아니면, 문자열로 join하는게 빠름그러니까 리스트안에 문자열로 저장, 그리고나서 문자열을 int로 가기
                                                                #3cnt: 교환을 수행한 횟수, cnt번째 각 요소간 교환을 수행하는 함수
def solve(cnt):
    global max_value
    global count
    num = int(''.join(data))
    count += 1
    if num in check:                                        # 12 교환해본 케이스니까 교환하지 않는다, return-교환하지 않은 케이스면 해본다
        check.add((cnt, num))
        return


    if cnt == N:
        # 6  교환이 완료된상태에서 결과를 확인하기
        # print(data)                                             # 10 data 확인하고, data를 숫자로 만들어 min_value와 비교하기
        if num > max_value:
            max_value = num
        return                                                 #5 교환이 필요하지않으니까 여기서 return해주기
    #4 교환 > 수행 후 재귀적으로 cnt + 1번째 교환을 수행한다.
    # 5 모든 요소에 대해서 요소 보다 뒤에 있는 요소와 교환하기:  i번째 요소는 i+1번쨰 요소에서
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            data[i], data[j] = data[j], data[i]
            solve(cnt+1)                                        # 7 cnt +1 번째 요소를 돈다
            data[i], data[j] = data[j], data[i]                 # 8 if cnt == N이후의 상황을 생각해보면. 다시 돌려놔야한다는 생각..


T = int(input())
for tc in range(1, T+1):
    data, N = input().split()
    data = list(data)
    N = int(N)
    max_value = 0                                                   # 11 비교할 거니까,
                                                                    # 2 요소의 개수가 정해져있지않으므로 반복문말고 재귀로 가보
    check = set()
    count = 0
    solve(0)                                                        # 9 교환을 아직 한번도 안했으니까. 0으로 하자

    #11 중복을 줄이기, 몇번째 교환 즉 k번째 교환에서 나온 결과가 중복되지말아야할것, value로 하는것이 아니라 k라는 횟수도 생각하기...
    print(count)
    print(f'#{tc} {max_value}')