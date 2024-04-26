w=int(input('enter wegiht of watermellon '))
if (w%2!=0):
    print('no')
else:
    x=w/2
    if(x%2==0):
        print("x1=",x, "and" "x2=",x)
    else:
        print("x1=",x-1,"and" "x2=",x+1)

fruits=['apple','banana','mango']
for i in fruits:
    print(i)

        
for num in range(2,20):
    if num%2==0:
        print(num)
        
num=int(input("Enter the number"))
count=0
while num !=0:
    num=num//10
    count=count+1
print('Number of digits:',count)

n=int(input('enter the number'))
sum=0
for i in range(1,n+1):
    sum=sum+i
print('sum of first n natural numbers:',sum)

num=12
num=int(input('display the multiplication table'))
for i in range(1,11):
    print(num,'x',i, "=",num*i)

n=int(input('enter the number'))
fact=1
for i in range(1,n+1):
    fact*=i
print('the factorial number is:',fact)
    