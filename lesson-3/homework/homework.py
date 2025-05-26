#LIST 
#1
a=list(map(str,input().split()))
b=input("Insert an element: ")
c=a.count(b)
print(f"This element occured {c} times in the given list")
#2
a=list(map(int,input("Sonlarni kiriting: ").split()))
print(sum(a))
#3
a=list(map(int,input("Sonlarni kiriting: ").split()))
print(max(a))
#4
a=list(map(int,input("Sonlarni kiriting: ").split()))
print(min(a))
#5
a=list(input())
b=input()
print(b in a)
#6
a=list(map(str,input().split()))
print(a[0])
#7
a=list(map(str,input().split()))
print(a[len(a)-1])
#8
a=list(map(str,input().split()))
print(a[:4])
#9
a=list(map(str,input().split()))
print(a[::-1])
#10
a=list(map(int,input().split()))
print(sorted(a))
#11
a=list(map(int,input().split()))
print(set(a))
#12
a=list(map(int,input().split()))
element=input("insert an element")
index=int(input("insert an index"))
a.insert(index,element)
print(a)
#13
a=list(map(int,input().split()))
element=int(input("Insert an element"))
print(a.index(element))
#14
a=list(map(int,input().split()))
print(len(a)==0)
#15
a=list(map(int,input().split()))
b=0
for i in range(len(a)):
    if a[i]%2==0:
        b+=1
print(f"{b} of them are even")
#16
a=list(map(int,input().split()))
b=0
for i in range(len(a)):
    if a[i]%2==1:
        b+=1
print(f"{b} of them are odd")
#17
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(a+b)
#18
a=list(map(int,input("Insert a list").split()))
b=list(map(int,input("Inser an sublist").split()))
print(b in a)
#19
a=list(map(int,input("Insert a list").split()))
b=int(input("Insert an element"))
d=int(input("Give an element to be replaced"))
c=a.index(b)
a[c]=d
print(a)
#20
a=list(map(int,input("Insert a list").split()))
a=sorted(a)
print(a[len(a)-2])
#21
a=list(map(int,input("Insert a list").split()))
a=sorted(a)
print(a[1])
#22
a=list(map(int,input("Insert a list").split()))
b=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(b)
#23
a=list(map(int,input("Insert a list").split()))
b=[]
for i in range(len(a)):
    if a[i]%2==1:
        b.append(a[i])
print(b)
#24
a=list(map(int,input("Insert a list").split()))
print(len(a))
#25
a=list(map(int,input("Insert a list").split()))
print(a.copy())
#26
from math import *
a=list(map(int,input("Insert a list").split()))
print(a[int(abs((len(a))/2))] if len(a)%2==1 else (a[int(len(a)/2-1)] , a[int(len(a)/2)]))
#27
st=int(input())
end=int(input())
a=list(map(int,input("Insert a list").split()))
print(max(a[st:end]))
#28
st=int(input())
end=int(input())
a=list(map(int,input("Insert a list").split()))
print(min(a[st:end]))
#29
a=list(map(int,input("Insert a list").split()))
b=int(input("Insert an index"))
if len(a)-1>=b:
    a.pop(b)
    print(a)
else:
    print(a)
#30
a=list(map(int,input("Insert a list").split()))
print(a==sorted(a))
#31
a=list(map(int,input("Insert a list").split()))
n=int(input("Insert a number"))
print(a*n)
#32
a=list(map(int,input("Insert a list").split()))
b=list(map(int,input("Insert a list").split()))
print(sorted(a+b))
#33
a=list(map(int,input("Insert a list").split()))
b=int(input("Insert an element"))
d=[]
c=0
for i in range(len(a)):
    if b in a:
        d.append(a.index(b)+c)
        c+=1
    else:
        break
    a.pop(a.index(b))
print(d)
#34
a = list(map(int, input("Enter a list of numbers for task 34: ").split()))
c=a[0]
a[0]=a[len(a)-1]
a[len(a)-1]=c
print(a)
#35
a=int(input("Input starting "))
b=int(input("Input ending "))
print(list(range(a,b+1)))

#36
a = list(map(int, input().split()))
c=0
for i in range(len(a)):
    if a[i]>0:
        c+=a[i]
print(c)
#37
a = list(map(int, input("Enter a list of numbers for task 35: ").split()))
c=0
for i in range(len(a)):
    if a[i]<0:
        c+=a[i]
print(c)
#38
a=list(map(int,input().split()))
print(a==a[::-1])
#39
size_39 = int(input("Enter the size of sublists for task 39: "))
task_39 = list(map(int, input("Enter a list of numbers for task 39: ").split()))
nested_list = [task_39[i:i + size_39] for i in range(0, len(task_39), size_39)]
print("Nested list:", nested_list)
#40
a=list(map(int,input().split()))
print(sorted(set(a)))

#TUPLE QUESTIONS
#1
a=tuple(map(int,input().split()))
b=int(input("Insert an element"))
print(a.count(b))
#2
a=tuple(map(int,input().split()))
print(max(a))
#3
a=tuple(map(int,input().split()))
print(min(a))
#4
a=tuple(map(int,input().split()))
b=int(input("Insert an element"))
print(b in a)
#5
a=tuple(map(int,input().split()))
print(0 if len(a)==0 else a[0])
#6
a=tuple(map(int,input().split()))
print(0 if len(a)==0 else a[len(a)-1])
#7
a=tuple(map(int,input().split()))
print(len(a))
#8
a=tuple(map(int,input().split()))
print(a[0:3])
#9
a=tuple(map(int,input().split()))
b=tuple(map(int,input().split()))
print(a+b)
#10
a=tuple(map(int,input().split()))
print(len(a)>1)
#11
a=tuple(map(int,input("Insert a tuple").split()))
b=int(input("Insert an element"))
d=[]
c=0
for i in range(len(a)):
    if b in a:
        d.append(a.index(b)+c)
        c+=1
    else:
        break
    a.pop(a.index(b))
print(d)
#12
a=tuple(map(int,input("Insert a tuple").split()))
print(sorted(a)[len(a)-2])
#13
a=tuple(map(int,input("Insert a tuple").split()))
print(sorted(a)[1])
#14
a=int(input())
print("Single element tupe is" , a)
#15
a=list(map(int,input().split()))
print(tuple(a))
#16
a=tuple(map(int,input().split()))
print(a==sorted(a))
#17
a=tuple(map(int,input("Insert a tuple").split()))
b=int(input("insert start"))
d=int(input("insert end"))
print(max(a[b:d+1]))
#18
a=tuple(map(int,input("Insert a tuple").split()))
b=int(input("insert start"))
d=int(input("insert end"))
print(min(a[b:d+1]))
#19
a=tuple(map(int,input().split()))
b=int(input("insert an element"))
a=list(a)
a.pop(a.index(b))
print(tuple(a))
#20
size_39 = int(input("Enter the size of sublists for task 20: "))
task_39 = tuple(map(int, input("Enter a list of numbers for task 20: ").split()))
nested_list = [task_39[i:i + size_39] for i in range(0, len(task_39), size_39)]
print("Nested tuple:", nested_list)
#21
a=tuple(map(int,input().split()))
n=int(input("Enter a number"))
print(a*n)

#22
a=int(input("Input starting "))
b=int(input("Input ending "))
print(tuple(range(a,b+1)))

#23
a = tuple(map(int, input().split()))
a=list(a)
c=a[0]
a[0]=a[len(a)-1]
a[len(a)-1]=c
print(tuple(a))

#24
a = tuple(map(int, input().split()))
a=list(a)
print(a==a[::-1])
#25
a = tuple(map(int, input().split()))
a=list(a)
print(tuple(sorted(set(a))))



