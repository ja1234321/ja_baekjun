# 요소가 1개라면, 정렬되어잇다고 보면된다...정렬되어있는 애들끼리는 비교-merge가능
# 정렬되어있는 2개의 배열이 필요, 최소단위
def merge(left, right):# 리스트 2개 받아서 정렬, 병합해 하나의 리스트를 만드는 함수
    result = []

    while left and right:# 비교=> 둘다 요소가 있을 때 비
        if left[0] < right[0]: # 비교는 이렇게 하면 됨(리스트의 값으로)
            result.append(left.pop(0)) # merge
        else:
            result.append(right.pop(0)) # merge
    if left:
        result += left                  # merge
        # result.extend(left)
    else:
        result += right                 # merge
    return result


def merge_sort(lst): # 리스트를 받아서 정렬해 반환하는 함수(
    N = len(lst)
    if N==1:
        return lst
    middle = N//2
    left = lst[:middle]
    right = lst[middle:] # 정렬 전 리스트
    left = merge_sort(left)
    right = merge_sort(right)   # 정렬 후 리스트
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    arr= list(map(int, input().split()))

    result = merge_sort(arr)
    print(result)
