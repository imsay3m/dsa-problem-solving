l = [i for i in input().split(" ")]
if l[1] == ">":
    if l[0] > l[2]:
        print("Right")
    else:
        print("Wrong")
elif l[1] == "=":
    if l[0] == l[2]:
        print("Right")
    else:
        print("Wrong")
elif l[1] == "<":
    if l[0] < l[2]:
        print("Right")
    else:
        print("Wrong")
