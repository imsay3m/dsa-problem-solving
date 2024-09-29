x = float(input())
if int(x) == float(x):
    print("int", int(x))
else:
    print(f"float {int(x)} {(x-int(x)):.3f}")
