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
a=int(input("Birinchi sonni kiriting:"))
b=int(input("Ikkinchi sonni kiriting:"))
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
#2
txt = 'LMaasleitbtui'
print("Malibu")
print("Lasetti")
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
print("So'zlari soni:" , len(a.split()))
#11
text = input("Matn kiriting: ")
print("Raqam bor" if any(char.isdigit() for char in text) else "Raqam yo'q")
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
a=input()
a=a.split()
b=''
for i in range(len(a)):
    b+=a[i][0]
print(b)
#16
a=input("Matn kiritng:")
b=input("Qaysi belgi olib tashlansin:")
a=a.split(b)
c=''
for i in range(len(a)):
  c+=a[i]
print(c)
#17
#18
a=input("Matnni kiriting:")
a=a.split()
print("Boshlanadi:", a[0])
print("Tugaydi: ", a[len(a)-1])
#BOOLEAN
#1
a=input("Usernmae kiriting:")
b=input("Password kiriting:")
c=0
if len(a)>0:
    c+=1
if len(b)>0:
    c+=1
print(f"{c} tasiga malumot kiritilgan")
#2
a=float(input("Birinchi sonni kiiritng:"))
b=float(input("Ikkinchi sonni kiriting:"))
print("Ikkalasi teng" if a==b else "Teng emas")

#3
a=float(input("Birinchi sonni kiiritng:"))
if a>0:
    c="The number is positive"
else:
    c="The number is not positive"
if a%2==0:
    b="The number is even"
else:
    b="The number is not even"
print(f"{c} and {b}")

#4
a=int(input("Input the first number: "))
b=int(input("Input the second number: "))
c=int(input("Innput the third number: "))
print("All the numbers are equal" if (a==b and b==c) else "All numbers are not equal")

#5
a=input("Input a text: ")
b=input("Input the second text: ")
print("They have the same length" if len(a)==len(b) else "They dont have the same length")
    
#6
a=int(input("Input an integer: "))
c=''
b=''
if a%3==0:
    c="It is divisible by 3"
if a%5==0:
    b="It is divisible by 5"
print("It is not divisible by neither 5 nor 3" if len(c+b)==0 else f"{c} {b}")
#7
a=float(input("Input the first integer: "))
b=float(input("Input the second integer: "))
print("Their sum is greater than 50.8" if a+b>50.8 else "Their sum is not greater than 50.8")
c=float(input("Enter a number: "))
print("This number is between 10 and 20" if 10<=c<=20 else "This number is not between 10 and 20")


