#1
list1 = [1, 1, 2]
list2 = [2, 3, 4]
list10=[]
for i,j in zip(list1,list2):
    if i not in list2:
        list10.append(i)
    if j not in list1:
        list10.append(j)
print(list10)
#2
n=int(input())
for i in range(1,n):
    print(i**2)
#3
txt=input("enter text: ")
i=3
oo=[]
uu=["a","u","e","i","o"]
while i<len(txt)-1:
    if txt[i-1] not in uu:
        if txt[i-1] not in oo:
            txt=txt[:i]+"_"+txt[i:]
            oo.append(txt[i-1])
            i+=4
        else:
            i+=1
    else:
        i+=1
print(txt)

#4
import random
a=['Y', 'YES', 'y', 'yes', 'ok']
b="Y"
while b in a:
    c=0
    while c<10:
      rn=random.randint(1, 100)
      gu=int(input("Guess the number from 1 to 100 "))
      if gu>rn:
          c+=1
          print("Too high")
    
      elif gu<rn:
          c+=1
          print("Too low")
      elif gu==rn:
          print("You won ")
          break
      if c==10:
          b=input("You lost. Want to play again? ")
    

#5
b=input("Enter your password ")
if len(b)<8:
    print("Your password is too short")
if b==b.lower():
    print("It must contain at least one uppercase ")
if len(b)>=8 and  b!=b.lower():
    print("It is strong")
#6
a=[]
for i in range(2,101):
    n=0
    for j in range(1,i):
       if i%j==0:
           n+=1
    if n==1:
        a.append(i)
print(a)
