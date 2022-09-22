import sys
sys.stdin = open('1946_input.txt', 'r')
sys.stdout = open('1946_output.txt', 'w')

for tc in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    print('#{}'.format(tc))
    for i in range(N):
        C, K = input().split()
        K = int(K)
        for j in range(K):
            print(C, end='')
            cnt += 1
            if cnt == 10:
                print()
                cnt = 0
    print()

