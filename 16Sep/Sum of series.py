#To find the sum of series upto given number with step of 2..
num = int(input('Enter the number upto which u wanna see the sum:'))
initial = 1
result = 0
while initial <= num:
    result += initial
    initial += 1
print('The sum upto given number is : ', result)
