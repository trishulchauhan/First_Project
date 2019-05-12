def bracket(string):
    l=len(string)
    rev=[]
    good=[]
    for i in range(0,l):
        good.append(string[i])
    for i in range(l-1,-1,-1):
        rev.append(string[i])
    c=0
    for i in range(0,l):
        if good[i]==rev[i] :
            c=c+1
        else:
            c=l+40
    if(c==l):
        print("hi")
    else:
        print("bye")

bracket("{([)]}")