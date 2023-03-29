'''백준1330
a,b=input("").split()
if int(a) < int(b):
    print("<")
if int(a) > int(b):
    print(">")
if int(a) == int(b):
    print("==")
'''

'''백준2750
a=int(input(""))
list=[]
for j in range(0,a):
    b=int(input(""))
    list.append(b)
list.sort()
for i in range(0,a):
    print(list[i])
'''



'''백준15964
a,b=input("").split()
print((int(a)+int(b))*(int(a)-int(b)))
'''

list=[]
c=1
for i in range(28):
    while c <= 30:
        list.append(c)
        c=c+1
    a=int(input(""))
    list.remove(a)
list.sort()
for j in range(len(list)):
    print(list[j])
    
'''
a=[]
b=0
c=1
while b<28:
    while c <= 30:
        a.append(c)
        c=c+1
    q=int(input(""))
    a.remove(q)
    b=b+1
c=0
while c<len(a):
    print(a[c])
    c=c+1
'''
'''백준5597
c=0
d=0
b=[]
while d <28:
    while c<28:
        a=input("")
        c=c+1
        b.append(a)
        print(b)
    d=d+1
    b.sort()
    if str(d) in b:
        continue
    else:
        print(d)
'''