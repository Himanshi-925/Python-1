#To find the sum of series upto given number..
num = int(input('Enter the number upto which u wanna see the sum:'))
i = 1
r = 0
while i <= num:
    r += i
    i += 1
print('The sum upto given number is : ', r)
