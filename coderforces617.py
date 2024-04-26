x=int(input('enter the min step at the point of x '))
if (x < 5):
    print(1)
elif (x % 5 == 0):
    print(x/5)
else:
    print(x//5+1) 