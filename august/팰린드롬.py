T = int(input())

for num in range(T):
    num = int(num) + 1
    word = input()
    reverse_word = word[::-1]
    if word == reverse_word:
        print(f'#{num} 1')
    elif word != reverse_word:
        print(f'#{num} 0')
