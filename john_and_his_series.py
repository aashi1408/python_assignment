#John_and_his_series
#first we'll input : a(the first term of the series)
#d(the common difference) and n(upto where we have to find the series)
a = int(input())
d = int(input())
n = int(input())
b = a+(n-1)*d#the AP eqn

sum = 0
for g in range(a,b,d):
    sum+=g
    print(g,end=' ')
print("Sum upto nth term = ",sum)//printing the sum upto nth term

