def is_armstrong(num):
    original_num = num
    armstrong_sum=0
    num_digits=len(str(num))
    while num > 0:
        digit = num % 10
        armstrong_sum += digit ** num_digits
        num//=10
    if (original_num == armstrong_sum):
         print("it is armstrong number")
    else:
         print("it is not armstrong number")
n=int(input('enter the number'))
is_armstrong(n)