# partition: pivot 을 잡고, 큰 값과 작은 값으로 나누고>피벗보다 작은 값을 퀵정렬, 피벗보다 큰 값을 퀵 정렬>단요소가 하나이면 멈추기> 반환은 피벗의 위치

def partition(left_index, right_index):
    # 1 - 1 ) 피벗은 임의로,
    pivot_index = left_index
    pivot = arr[pivot_index]
    i_index, j_index = left_index, right_index # 움직일 초점같은거
    # ( i_index, j_index 각각 증가 감소하며 pivot 보다 각각 큰값, 작은값 찾기- 위치 교환)
    while i_index <= j_index:
        while i_index <= j_index and arr[i_index] <= pivot:
            i_index += 1
        while i_index <= j_index and arr[j_index] >= pivot:
            j_index -= 1
        # i_index 와 j_index가 역전되면 멈출것이다
        # swap
        if i_index < j_index:
            arr[i_index], arr[j_index] = arr[j_index], arr[i_index]
    arr[pivot_index] , arr[j_index] = arr[j_index], arr[pivot_index]
    return j_index



def quick_sort(l, r): # 피벗과
    # ㅣ과 r은 인덱스
    if l<r:
        # 먼저 partition
        p_index = partition(l,r) # 피벗은 자기 위치가 있으므로, 정렬에 포함하지 않음
        # 피벗을 기준으로 작은 값과 큰 값을 다시 정렬,
        quick_sort(l, p_index-1)
        quick_sort(p_index+1, r)

arr = [9,1,2,3]
quick_sort(0, len(arr)-1)
print(arr)