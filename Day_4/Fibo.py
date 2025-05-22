def fibo_seq(n):
    fib_series=[]
    a,b=0,1
    for _ in range(n):
        fib_series.append(a)
        a,b=b,a+b
    return fib_series
n=int(input('Enter the number upto nTH term'))
if n<=0:
    print('PLEASE ENTER THE POSITIVE NUMBER')
else:
    print(f'The fibonacci series up to nTH term is {fibo_seq(n)}')