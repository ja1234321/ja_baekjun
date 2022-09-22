a, b = list(map(int, input().split()))

def rock_paper_scissors(a, b):
    if a == 1:
        if b == 2:
            print('B')
        elif b == 3:
            print('A')
    elif a == 2:
        if b == 3:
            print('B')
        elif b == 1:
            print('A')
    elif a == 3:
        if b == 1:
            print('B')
        elif b == 2:
            print('A')

rock_paper_scissors(a, b)