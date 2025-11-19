#max_of_three

m = int(input())
n = int(input())
o = int(input())

if m==n and n==o :
    print("All are same")
if ((m==n or n==o) or m==o):
    print(max(m,n,o))
mx = m if(m>n and m>o) else n if(n>m and n>o) else o
print(mx)