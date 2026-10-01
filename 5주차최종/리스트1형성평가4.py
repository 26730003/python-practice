n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
avg = sum(lst) // n
print(avg)
