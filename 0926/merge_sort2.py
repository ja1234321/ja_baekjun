# sprig merge_sort()에서 l,r 의 인덱스 조정으로,
def merge2(l,r):
    left_index = l
    middle_index = (l+r)//2
    right_index = middle_index + 1
    merged_lst=[]
    while left_index <= middle_index and right_index <= r:
        if arr[left_index] < arr[right_index]:
            merged_lst.append(arr[left_index])
            left_index += 1
        else:
            merged_lst.append(arr[right_index])
            right_index += 1
    if left_index <= middle_index:
        for a in range(left_index, middle_index+1):
            merged_lst.append(arr[a])
    if right_index <= r:
        for a in range(right_index, r+1):
            merged_lst.append(arr[a])
    # merged를 arr에 복사하기. 여기*********************************
    idx = 0
    for x in range(l, r+1):
        arr[x] = merged_lst[idx]
        idx += 1


def merge_sort2(left, right): #각각의  정렬대상 인덱스
    if right==left:
        return
    middle = (left + right)//2
    merge_sort2(left, middle)
    merge_sort2(middle+1, right)
    merge2(left, right)


arr = [2,9,3,1]
N = len(arr)
# merge_sort(0, N-1)
merge_sort2(0, N-1)
print(arr)