w=[x for x in input().split(' ')]

if w[1]=='+':
    print("Yes") if (int(w[0])+int(w[2])==int(w[4])) else print(int(w[0])+int(w[2]))
elif w[1]=='-':
    print("Yes") if (int(w[0])-int(w[2])==int(w[4])) else print(int(w[0])-int(w[2]))
elif w[1]=='*':
    print("Yes") if (int(w[0])*int(w[2])==int(w[4])) else print(int(w[0])*int(w[2]))