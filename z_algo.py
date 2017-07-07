def z_arr(ss):
    l=0
    r=0
    k=0
    n=len(ss)
    z=[0]
    for i in range(1,n):
        if l<i:
            l=r=i
            while(r<n and ss[r-l]==ss[r]):
                r+=1
            z.append(r-l)
            r-=1
        else:
            k=i-l
            if z[k]<r-i+1:
                z.append(z[k])
            else:
                l=i
                while r<n and ss[r-l]==ss[r]:
                    r+=1
                z.append(r-l)
                r-=1
    return z
def search(ss,pattern):
    concate=pattern+'$'+ss
    z=z_arr(concate)
    for i in range(len(z)):
        if z[i]==len(pattern):
            print("pattern found at index ",i-len(pattern)-1)

text = "GEEKS FOR GEEKS"
pattern = "GEEK"
search(text, pattern)
