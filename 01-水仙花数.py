print ('please input number')
num = input()
int_num = int(num)
sum_num = 0
for i in num:
    sum_num += int(i)**len(num)

if int_num == sum_num:
    print ('this is Narcissistic number')
else:
    print ("this isn't Narcissistic number")
