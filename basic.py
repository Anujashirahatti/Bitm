a=10
b=20
c=a+b
print(c)
total=0
for i in range(10):
    total=total+i
    print(total)
thisdict={'size':'fat','color':'black','year':1999}
print(thisdict)
n=thisdict['movie']='bahubali'
print(n)
thisdict.update({'color':'black'})
print(thisdict)
del thisdict['size']
print(thisdict)
list=['apple','cake','banana']
print(list)
l=['abc',1,2,'True']
l.append('apple')
l.insert(-2,'cat')
l.remove('apple')
print(l)
k=('apple','cat','elephant')
print(type(k))
print(id(k))
t=['123']+['apple','orange']
print(t)
print('alice'*5)
print('alice'+'bob')
s='dox'
print(s*2)
p='aliya'
print(p+'dad')
import random,sys
print('rock','papaer','scissors')
wins=0
losses=0
ties=0
while True:
    print('enter your movie:(r)ock,(p)aper,(s)cissors or quit')
    playerMove=input()
    if playerMove=='q':
        sys.exit()
if playerMove=='r' or playerMove=='p'or playerMove=='s':
    break
print('any one type r,p,s,q') 
if playerMove=='r':
    print('Rock verses')
elif playerMove=='p':
    print('paper verses')
elif playerMove=='s':
    print('scissors verses')
randomNumber=random.randint(1,3)
if randomNumber=='1':
    computerMove='r'
    print('Rock')
elif randomNumber=='2':
    computerMove='p'
    print('paper')
elif randomNumber=='3':
    computerMove='s'
    print('scissor')
if playerMove==computerMove:
    print('it is ties')
    ties=ties+1
elif playerMove=='r' and computerMove=='s':
    print('you wins')
    wins=wins+1
elif playerMove=='s' and computerMove=='r':
    print('you losses')
    losses=losses+1
name=''
print('what is your name')
while True:
    print('please enter your name')
    name=input()
    print(name)
for i in range(4):
    print(i)


    


