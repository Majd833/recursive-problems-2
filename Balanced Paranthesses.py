def par(s,l,r,p,n):
    if p==2*n:
        for ss in s:
            print(ss,end=" ")
        print("\n")
        return
    if l>r:
        s[p]="}"
        par(s,l,r+1,p+1,n)
    if l<n:
        s[p]="{"
        par(s,l+1,r,p+1,n)
n=int(input("Enter the number of parenthesses:"))
s=[""]*2*n
print("\n")
print(par(s,0,0,0,n))