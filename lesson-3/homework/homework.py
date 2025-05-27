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
#SET Tasks
#1
s1={'a','b','c','d'}
s2={'1','2','3','4','5'}
print(s1.union(s2))
#2
print(s1&s2)
#3
print(s1.difference(s2))
#4
print(s1 in s2)
#5
b=input("Input an element for task 5 ")
print(b in s1)
#6
print(len(s1))
#7
a=list(map(str,input('enter list for task 7 ').split()))
print(set(a))
#8
s=set(map(str,input("Enter set for task 8 ").split()))
b=input("Enter an element to remove ")
if b in s:
    s.remove(b)
    print(s)
else:
    print("This element is not available in this set")
#9
s=set(map(str,input("Enter set for task 9 ").split()))
s.clear()
print("Cleared set :", s)
#10
s=set(map(str,input("Enter set for task 10 ").split()))
print(len(s)==0)
#11
s1={'a','b','c','d'}
s2={'1','2','3','4','5'}
print(s1.symmetric_difference(s2))
#12
s=set(map(str,input("Enter set for task 12 ").split()))
b=input("Input an element for task 12 ")
if b in s:
    print("It is already in it ")
else:
    s=list(s)
    s.append(b)
    print(set(s))
#13
s=set(map(str,input("Enter set for task 13 ").split()))
print(s.pop())
#14
s=set(map(str,input("Enter set for task 14 ").split()))
print(max(s))
#15
s=set(map(str,input("Enter set for task 15 ").split()))
print(min(s))
#16
s=set(map(int,input("Enter set for task 16 ").split()))
s=list(s)
a=[]
for i in range(len(s)):
    if s[i]%2==0:
        a.append(s[i])
print(set(a))
#17
s=set(map(int,input("Enter set for task 17 ").split()))
s=list(s)
a=[]
for i in range(len(s)):
    if s[i]%2==1:
        a.append(s[i])
print(set(a))
#18
a=int(input("Input starting point "))
b=int(input("Input ending point "))
print(set(range(a,b)))
#19
a=list(map(str,input("Enter the first list for task 19 ").split()))
b=list(map(str,input("Enter the second list for task 19 ").split()))
print(set(a+b))
#20
s=set(map(int,input("Enter set for task 20 ").split()))
s2=set(map(int,input("Enter set for task 20 ").split()))
print(len(s&s2)==0)
#21
s=list(map(int,input("Enter list for task 21 ").split()))
print(list(set(s)))
#22
s=list(map(int,input("Enter list for task 22 ").split()))
print(len(set(s)))
#23
import random
s = {random.randint(1, 100) for _ in range(10)}
print(s)
#DICT Tasks
dict_1 = {"a": 1, "b": 2, "c": 3}
key_1 = input()
print(dict_1.get(key_1, "Key not found"))

key_2 = input()
print(key_2 in dict_1)

print(len(dict_1))

print(list(dict_1.keys()))

print(list(dict_1.values()))

dict_2 = {"d": 4, "e": 5}
merged_dict = dict_1.copy()
merged_dict.update(dict_2)
print(merged_dict)

key_4 = input()
dict_1.pop(key_4, None)
print(dict_1)

dict_5 = {}
print(len(dict_5) == 0)

key_6 = input()
print({key_6: dict_1.get(key_6)} if key_6 in dict_1 else "Key not found")

key_7 = input()
value_7 = input()
dict_1[key_7] = value_7
print(dict_1)

value_8 = input()
print(list(key for key, value in dict_1.items() if value == value_8))

keys_list = list(input().split())
values_list = list(input().split())
new_dict = dict(zip(keys_list, values_list))
print(new_dict)

print(any(isinstance(value, dict) for value in dict_1.values()))

nested_dict = {"a": {"x": 10}, "b": {"y": 20}}
key_9 = input()
nested_key_9 = input()
print(nested_dict.get(key_9, {}).get(nested_key_9, "Not Found"))

default_dict = dict.fromkeys(["a", "b", "c"], 0)
print(default_dict)

print(len(set(dict_1.values())))

sorted_dict_by_key = dict(sorted(dict_1.items()))
print(sorted_dict_by_key)

sorted_dict_by_value = dict(sorted(dict_1.items(), key=lambda item: item[1]))
print(sorted_dict_by_value)

filtered_dict = {key: value for key, value in dict_1.items() if value > 1}
print(filtered_dict)

dict_10 = {"a": 1, "b": 2}
dict_11 = {"b": 2, "c": 3}
print(bool(dict_10.keys() & dict_11.keys()))

tuple_12 = (("a", 1), ("b", 2))
dict_from_tuple = dict(tuple_12)
print(dict_from_tuple)

print(next(iter(dict_1.items())))
