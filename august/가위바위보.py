# input() : 입력을 받음
# .split('/') : /를 기준으로 가름, 없다면 띄어쓰기를 기준으로 나눔
# data = input().split() :  결과가 str의 리스트 형태로 나옴 ['3','2']
# map( , ) : 각각의 data의 리스트를 int형으로 바꿔준다는 것
# list() : list의 형태로 변화까지 시켜준 것

data = list(map(int, input().split()))
# 3 2를 넣은 결과는 [3, 2]

# 1: 가위, 2: 바위, 3: 보
# data[0]을 기준으로 검사
# 1 이라면, data[1]이 2면 지는거, 3이면 이기는거
# 2 이라면, data[1]이 3면 지는거, 1이면 이기는거
# 3 이라면, data[1]이 1면 지는거, 2이면 이기는거

winner = 'A'
if data[0] == 1:
    if data[1] == 2:
        winner = 'B'
elif data[0] == 2:
    if data[1] == 3:
        winner = 'B'
else:
    if data[1] == 1:
        winner = 'B'

print(winner)
