def check_bg(lst, p):
    tri = run = 0
    if lst[0] == lst[1] and lst[1] == lst[2]:
        tri += 1
    if lst[0]+1 == lst[1] and lst[1] + 1 == lst[2]:
        run += 1
    if lst[1] == lst[2] and lst[2] == lst[3]:
        tri += 1
    if lst[1]+1 == lst[2] and lst[2] + 1 == lst[3]:
        run += 1
    if tri:
        return True
    if run:
        return True
    return False


arr = list(map(int, input().split()))
p1= []
p2= []
for i in range(0,12,2):
    p1.append(arr[i])
    p2.append(arr[i+1])
pin1 = 2
pin2 = 2
while True:
    if check_bg(p1, pin1):
        pass
        result = 1
    else:
        pin1 += 1
    if check_bg(p2, pin2):
        result = 0
    else:
        pin2 += 1
    if pin2 == 6:
        result = 0