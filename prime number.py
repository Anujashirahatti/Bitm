num=10
if num==1:
    print(num,"is not prime number")
elif num > 1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is prime number")