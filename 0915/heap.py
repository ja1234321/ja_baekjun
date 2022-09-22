heap = [None] * 16                  # 최대 높이가 3인 heap
heap_count = 0                           # the last 원소를 가리키는 병수, que: front, rear,  stack: top; 0 이면 노드가 없음을 의미함.


def heap_push(value):
    # 마지막 위치에 value 넣기
    global heap_count
    heap_count += 1
    heap[heap_count] = value
    #  부모노드랑 비교해서 자식 노드가 더 크면 바꿔주기(반복)
    current = heap_count
    parent = current//2
    # 현재 노드가 root가 아니고, 자식 노드가 부모보다 더 크면 바꿈...
    while current > 1 and heap[current]> heap[parent]:
        heap[current], heap[parent] = heap[parent], heap[current] #  바꿔주기...
        current = parent
        parent = current // 2
    pass


def heap_pop():
    global heap_count
    result = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = None
    heap_count -= 1

    parent = 1
    child = parent * 2 # 왼쪽 자식은 항상 존재하니까 왼쪽 먼저 접근
    if child + 1 <= heap_count: # 오른쪽 자식이 존재하면
        if heap[child] < heap[child+1]:
            child += 1
    # parent 와 child 결정됨
    while child <= heap_count and heap[child] > heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = parent * 2
        if child + 1 <= heap_count:  # 오른쪽 자식이 존재하면
            if heap[child] < heap[child + 1]:
                child += 1
    # root 를 반환하기
    # 마지막 요소를 루트 위치에 복사하기
    # 자식노드와 비교해서 자식노드가 더 크면 바꿔주기(반복): 자식노드가 더 이상 없을때까지
    return result


heap_push(2)
heap_push(3)
heap_push(6)
heap_push(7)
heap_push(4)
heap_push(5)
print(heap_pop())