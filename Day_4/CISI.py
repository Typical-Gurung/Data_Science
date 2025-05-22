def CI(p,t,r):
    return p*((1+r/100)**t-1)
def SI(p,t,r):
    return (p*t*r)/100
p=float(input("Enter the principal"))
t=float(input("Enter the time"))
r=float(input("Enter the rate"))

si=SI(p,t,r)
ci=CI(p,t,r)
d=ci-si
print(f'The simple interest of the data is:{si:.2f}')
print(f'The compound interest of the data is:{ci:.2f}')
print(f'The difference of the data is:{d:.2f}')
