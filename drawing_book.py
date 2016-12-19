n = int(input().strip())
p = int(input().strip())

front = True
cur_page = 1
if p / n > 0.5:
    front = False
    cur_page = n

if front:
    flips = 0
    while p > cur_page:
        flips += 1
        cur_page += 2
else:
    if n % 2 != 0:
        flips = -1
    else:
        flips = 0
    while p < cur_page:
        flips += 1
        cur_page -= 2

print(flips)
