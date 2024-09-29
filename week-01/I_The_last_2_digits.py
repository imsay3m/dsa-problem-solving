l=[int(x) for x in input().split(' ')]

mul=1
for i in l:
    mul=mul*i
str_mul=str(mul)
print(str_mul[-2:])
