# l = [int(i) for i in input().split()]
l = list(map(int, input().split()))
l_new = sorted(l)
print(*l_new, sep="\n")
print("")
print(*l, sep="\n")
