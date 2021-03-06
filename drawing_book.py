# Solution to Drawing Book (https://www.hackerrank.com/contests/w27/challenges/drawing-book)
# We start off by checking if the page to flip to (p) is in the first half or second half of the book.
# if in first half, increment flip counter till right page is greater than p
# else increment flip counter till left page is lesser than (p - 1)

n = int(input().strip())
p = int(input().strip())

front = True
cur_page = 1

# Step 1: check which half of book
if p / n > 0.5:
    front = False
    cur_page = n

flips = 0
if front:
    # first half
    while p > cur_page:
        # till right page is greater than p
        flips += 1
        cur_page += 2
else:
    # left half
    while p < (cur_page - 1):
        # till left page is lesser than (p - 1)
        flips += 1
        cur_page -= 2

print(flips)
