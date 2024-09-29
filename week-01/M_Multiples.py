l=[int(x) for x in input().split(" ")]
print("Multiples" if l[0]%l[1]==0 or l[1]%l[0]==0 else "No Multiples")