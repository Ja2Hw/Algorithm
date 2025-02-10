L = int(input())
cake = [0] * (L + 1)
N = int(input())

want_pieces = 0
want_person = 0

for i in range(1, N + 1):
    p, k = map(int, input().split())
    if want_pieces < k - p:
        want_pieces = k - p
        want_person = i

    for j in range(p, k + 1):
        if cake[j] != 0:
            continue
        else:
            cake[j] = i

print(want_person)

max_pieces = 0
max_person = 0
for i in range(1, N + 1):
    if max_pieces < cake.count(i):
        max_person = i
        max_pieces = cake.count(i)
print(max_person)