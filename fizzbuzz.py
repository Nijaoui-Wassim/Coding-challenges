import math
print('give me the min')
x = input()
print('give me the max')
y=input()
i = 0
for i in range(int(x),int(y)):
    somme = 0
    digits = [int(x) for x in str(i)]
    for y in range (len(digits)):
        somme += int(digits[y])
    if (int(digits[-1]) == 5 or int(digits[-1]) == 0) and float(somme / 3).is_integer():
        print ('%d FizzBuzz' %(i))
    elif float(somme / 3).is_integer():
        print('Fizz')
    elif int(digits[-1]) == 5 or int(digits[-1]) == 0:
        print ('Buzz')
    else:
        print (i)

#digits = [int(x) for x in str(i)]

#for s in range (0,len(digits)):
#    total = total + digits[s]
