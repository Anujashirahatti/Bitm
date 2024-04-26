print('enter the correct username and password')
count=0
password='anu'
username='raju'
while password!='anu' and username!='raju':
    count<4
    password=input()
    username=input()
if password=='anu' and username=='raju':
    print('access granted')
else:
    print('retry')