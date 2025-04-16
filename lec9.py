#conditional statement:
#if
'''num = 10
if num > 5:
    print(" ")'''

#else
'''Num = 7
if num%2 == 0 :
   Print ("Even")
Else:
  Print ("odd")''' #odd

#elif: multiple condition :
#Elif - else if
'''If condition:
Code
Elif condition 2:
Code 
Else :
Code'''
#eg:
'''Score = 75
If score >= 90:
Print ("A")
Elif score>=70:
Print ("b")
Else:
Print ("c")'''

#nested if-else condition :
#eg:
'''if x > 5:
        if x==10:
        print('x is 10')
        else:
        print('x is not 10')
    else:
    print('x is less than 5')'''

#looping statement :
#for loop :
#syntax:for variable in sequence:
    #code
#eg:
    #For i in range (1, 5):
    #Print(i)

#while loop : perform code while the condition satisfies
'''syntax:
    While condition:
    count = 1
    While count<=3:
    print(count)
    count+=1
'''

#nested loop: loop within loop
#eg:
'''for i in range (1,3):
        for j in range(1,3):
            print ("i",i,"j",j)'''

#write any program for any number table :
'''n = int(input("Enter The number for table :- "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")'''

#keywords: pass (pass the code) and break (stop the execution of the code)
#eg:pass
'''a = 5
B = 10
If a>b
Pass
Else:'''

#break :
#eg:
'''x=10
for i in range(1,11):
    if i == 0:
        pass
    elif i == 4:
        continue
    elif i == 5:
        break
    else:
        print(i)'''
#eg2:
'''Str1 = "python"
for i in str1
    if I=='o':
    Break
    Print (I)'''

#eg3: continue statements skips the o words pass does not skips
'''Str1 = "python"
for i in Str1:
    if i =='o':
        continue
    print(i)'''

'''Today's assessment :
1.pyramid pattern using nested loop not by* but by any number
2.factorial program 15/20! using loop
3.sum of digits : while statement (eg : 12345 = 15 )
4.multiple of number:(while loop or continue) 2 and 3 divisible is should be skipped
n=5  print(5,10,20,25,35,40,50) 
means, all number which are divisible by 2 and 3 are skipped 
but which are not divisible by 2 and 3 then there divisible is shown
5.login system : current password (abc) wrong password throw an error and 
lock the account for attempts more than 3 or just print lock
'''


# Assessment
# eg: 1
'''rows = 5
for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(1, i+1):
        print(k, end="")
    for l in range(i-1, 0, -1):
        print(l, end="")
    print()'''

# eg: 2

'''def factorial_ratio(numerator, denominator):
    result = 1
    for i in range(denominator + 1, numerator + 1):
        result *= i
    return result

numerator = 20
denominator = 15
result = factorial_ratio(numerator, denominator)

print(f"The result of 20! / 15! is: {result}")'''

# eg: 3
'''number = int(input("Enter a number: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10            
print(f"The sum of the digits is: {sum_of_digits}")'''

# eg: 4

'''n= int(input("Enter any number"))
limit = int(input("Enter the limit"))
i = 1
while i * n <= limit:
    multiple = i * n
    if multiple % 2 == 0 and multiple % 3 == 0:
        i+=1
        continue
    print(multiple)
    i+=1'''

# eg : 5
'''current_password = 'abc'
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    enter_password = input("Enter your Password")

    if enter_password == current_password:
        print("Login successful!")
        break
    else:
        attempts +=1
        print(f"Wrong password! attempts left: {max_attempts - attempts}")

        if attempts == max_attempts:
            print("Phone locked, try later!")'''

c


