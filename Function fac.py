def factorial(k):
    fact=1
    for i in range(1,k+1):
        fact*=i
    return fact
n=int(input('the factorial number is '))
f=factorial(n)
print(f)
    
    
        