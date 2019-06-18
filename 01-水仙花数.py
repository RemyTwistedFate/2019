//在数论中，水仙花数（Narcissistic number）用来描述一个N位非负整数，其各位数字的N次方和等于该数本身。

print ('please input number')
num = input() int_num = int(num)
sum_num = 0
for i in num:
    sum_num += int(i)**len(num)

if int_num == sum_num:
    print ('this is Narcissistic number')
else:
    print ("this isn't Narcissistic number")
