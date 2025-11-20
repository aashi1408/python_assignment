#last_digit_of_a**b

N = int(input())#N is the count of the number pairs
for k in range(N):
    Q,R = map(int,input().split())
    pow_value = Q**R#Q to the power R
    ld = pow_value%10#modulo gives the last digit
    print(ld)