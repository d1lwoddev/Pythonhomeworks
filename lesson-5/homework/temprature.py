def convert_cel_far(F):
    C=(F-32)*5/9
    print(F,"degres F =",round(C,2)," degres C")

F=int(input("Enter a number in degres: "))
convert_cel_far(F)
def convert_far_cel(C):
    F=C*9/5+32
    print(C,"degres C =",round(F,2)," degre F")
    
C=int(input("Enter a number in degres: "))
convert_far_cel(C)
    
