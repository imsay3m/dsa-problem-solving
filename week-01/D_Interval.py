x = float(input())

if x >= 0 and x <= 100:
    print("Interval", end=" ")
    if x >= 0 and x <= 25:
        print("[0,25]")
    elif x > 25 and x <= 50:
        print("(25,50]")
    elif x > 50 and x <= 75:
        print("(50,75]")
    elif x > 75 and x <= 100:
        print("(75,100]")
else:
    print("Out of Intervals")
