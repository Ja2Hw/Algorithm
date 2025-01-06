import sys

word = sys.stdin.readline().strip().upper()

set_word = set(word)
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