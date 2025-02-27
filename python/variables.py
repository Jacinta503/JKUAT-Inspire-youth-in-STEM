#variables in python and data types
student_name ="Mandla" # string
student_second_name = 'Francisca' #string
student_age = 20 # interger
student_height = 1.65 # float
student_admitted = True # boolen
# Operators in Python
# Arithmetic operators
num1 = 15
num2 = 25
addition = num1 + num2
# print(addition)
subtraction = num2 - num1
# pint(subtraction)
print (num1 == num2 )
print (num1 != num2 )

#3. Logical operators
# and, or,  not
print(num1 < num2 and num1 > num2) # False

# 4. Assignment operators
# =, +=, -+, *=, /=
# num1 += 5
# print(num1) #20
# num1 -=5
# print (num1) #15
# num1 *= 5
# print (num1 ) #100

# 5. identity operators
# is, is not
print (num1 is not num2) # True
# print ( num1 is num2) # False

# 6. Conditional statement
# if, elif, else

if student_age >= 18:
    print("You are an adult")

enter_name = input("Enter your name: ")    
enter_age = int(input ("Enter your age: "))
if enter_age >= 18:
    print(enter_name, " is an adult")