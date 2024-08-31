n = int(input())

if n==5:
    for i in range(n):
        print('*' * (i+1))
elif n==6:
    for i in range(1, n+1):
        print(' ' * (n-i)+ '*' * i)
        
else:
    print('Invalid input(5 or 6)')