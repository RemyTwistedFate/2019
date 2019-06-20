print ('please input a number')
num = int(input())
sum = 0
for i in range(1,num):
    if num%i == 0:
        sum += i

if sum == num:
    print ('this is Perfect number')

