#data type questions
#1
from math import *
a=float(input())
print(round(a,2))
#2
a=float(input())
b=float(input())
c=float(input())
print("Maximum:" , max(a,b,c))
print("Minimum:" , min(a,b,c))
#3
a=float(input("Qiymatni kiriting:"))
print("Metrda:" , a*1000)
print("Santimetrda:" , a*100000)
#4
a=float(input("Birinchi sonni kiriting:"))
b=float(input("Ikkinchi sonni kiriting:"))
print("Bo'linmasi:" , int(a//b))
print("Qoldig'i:" , a%b)
#5
a=float(input("Celcius:"))
print("Farenheit:" , (a*(9/5))+32)
#6
a=float(input())
print(a%10)
#7
a=float(input())
if a%2==0:
    print("The number is even")
else:
    print("The number is not even")
#String questions
#1
a=input("what is your name?")
b=float(input("When were you born?"))
print("Your age is" , 2025-b)
#3
a=input()
print("Uzunligi:" ,len(a))
print("Katta harfda:" ,a.upper())
print("Kichik harfda:", a.lower())
#4
a=input()
if a[::-1]==a:
    print("Palindrome")
else:
    print("Not palindrome")
#5
a="aeiouаеёиоуыэюя"
c=input().lower()
unli=0
unsiz=0
for i in range(len(c)):
    if c[i] in a:
        unli+=1
    else:
        unsiz+=1
print("Vowels:" , unli)
print("Consonants:" , unsiz)
#6
a=input()
b=input()
if a in b or b in a:
    print("Bor")
else:
    print("Yo'q")
#7
a=input("Text kiriting:")
b=input("Almashtiriladigan so'zni kiritng:")
c=input("Qaysi so'z joyiga kiritilsin:")
print("Result: " , a.replace(b,c))
#8
a=input("Textni kiriting:")
print("Birinchi harfi:" ,  a[0])
print("Oxirgi harfi:" , a[len(a)-1])
#9
a=input("Textni kiriting:")
print("Teskari shakli:" , a[::-1])
#10
a=input("Gapni kiriting:")
print("So'zlari soni:" , len(gap.split()))
#11
a=input()
if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in a:
    print("Yes")
else:
    print("No")
#12
a=list(map(str,input().split()))
s=''
for i in range(len(a)):
    s=s+"-"+a[i]
print(s[1::])
#13
a=input()
print(a.replace(" ",""))
#14
a=input()
b=input()
if a==b:
  print("Equal")
else:
    print("Not equal")
#15
    
