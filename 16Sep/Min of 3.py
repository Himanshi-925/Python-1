#Minimun of given three number
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

if a < b and a < c:
    print(a, 'is smallest among given three numbers.')
elif b < c:
    print(b, 'is smallest among given three numbers.')
else:
    print(c, 'is smallest among given three numbers.')
