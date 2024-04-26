num=int(input('Enter the number '))
rev=0
while num > 0:
    digit=num % 10 #we get last digit of number
    rev=rev * 10 + digit
    num = num // 10
print("Reverse number",rev)


    
    

