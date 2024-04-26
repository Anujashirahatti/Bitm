def add_number(a,b):
    return a+b
result=add_number(4,5)
print(result)

def greet(name='world'):
    print('hello,'+name+'!')
greet()
greet('anu')

def greet(name,greeting):
    print(greeting+","+name+'!')
greet(greeting="hello",name='raju')

l=[1,3,4]
print(l)
print(*l)

def multiply(*args):
    result=1
    for num in args:
        result=result*num
    return(result)
print(multiply(2,3,4))

def addition(*args):
    result=0
    for num in args:
        result=result+num
    return(result)
print(addition(2,3,4))

def student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} {value}")
student(name='anu',age=19,clg='bitm')


