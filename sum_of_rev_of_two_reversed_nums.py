def reverse(d):
    rev = 0
    while(d!=0):
        ld = d%10
        rev = rev*10+ld
        d//=10
    return rev
    
N = int(input())#count of number pairs we are going to input
for j in range(N):
    a,b = map(int,input().split())
    rev1 = reverse(a)
    rev2 = reverse(b)
    ans = rev1 + rev2
    rev_ans = reverse(ans)
    print(rev_ans)