w=input()
w=w.replace('.','')
w=w.replace(',','')
w=w.replace('!','')
w=w.replace('?','')
w=list(w.split(' '))
w=[x for x in w if(x)]
print(len(w))