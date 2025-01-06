import sys

word = sys.stdin.readline().strip().upper()

set_word = set(word)

# 등장 횟수를 저장할 딕셔너리
count_dict = {char: word.count(char) for char in set_word}

# 최댓값 찾기
max_count = max(count_dict.values())

# 최댓값에 해당하는 문자 찾기
max_chars = [char for char, count in count_dict.items() if count == max_count]

# 출력
if len(max_chars) == 1:
    print(max_chars[0])
else:
    print("?")

"""
처음 풀어서 맞춘 방식

cnt = 0
only = True
for w in set_word:
    if word.count(w) > cnt:
        cnt = word.count(w)
        only = True
        res = w
    elif word.count(w) == cnt:
        only = False
    else:
        continue
if only:
    print(res)
else:
    print("?")
"""
