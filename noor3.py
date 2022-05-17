m=int(input("Please enter a decimal number:  "))
a=[]
if m==0:
    print(m)
else:
    while (m!=0):
        recent=m%2
        a.append(recent)
        m=m//2
a.reverse()
for z in range(0,len(a)):
    a[z]=int (a[z])
    print(a[z],end="")
            
