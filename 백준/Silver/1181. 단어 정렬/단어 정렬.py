#단어 정렬

n = int(input())
input_list = []
tmp = []
for _ in range(n):
    word = input()
    if word not in tmp:
        tmp.append(word)
        input_list.append([word, len(word)])

sorted_list = sorted(sorted(input_list), key=lambda x: x[1])
for s in sorted_list:
    print(s[0])