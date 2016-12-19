n = int(input().strip())
p = int(input().strip())

front = True
cur_page = 1
if p / n > 0.5:
    front = False
    cur_page = n

flips = 0
if front:
    while p > cur_page:
        flips += 1
        cur_page += 2
else:
    while p < (cur_page - 1):
        flips += 1
        cur_page -= 2

print(flips)
