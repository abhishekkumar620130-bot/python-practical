# ## SECTION 2: BOOLEAN QUESTIONS
# (True, False, Boolean expressions, and logic)
# 30 Questions

# 1. What is a Boolean value in Python?
# 2. What are the two Boolean constants?
# 3. What will be the output?
    
#     print(10 > 5)
    
# 4. What will be the output?
    
#     print(5 == 10)
    
# 5. What will be the output?
    
#     print(5 != 5)
    
# 6. What is the result of:
    
#     10 >= 10
    
# 7. What is the result of:
    
#     3 < 1
    
# 8. Take a number and print True if it is positive.
# 9. Take a number and print True if it is even.
# 10. Take age and print True if age >= 18.
# 11. What will be the output?
    
#     print(True and False)
    
# 12. What will be the output?
    
#     print(True or False)
    
# 13. What will be the output?
    
#     print(not True)
    
# 14. What will be the output?
    
#     print(not False)
    
# 15. What will be the output?
    
#     print(5 > 2 and 10 > 3)
    
# 16. What will be the output?
    
#     print(5 > 2 and 3 > 10)
    
# 17. What will be the output?
    
#     print(5 > 2 or 3 > 10)
    
# 18. Take two numbers and print True if both are positive.
# 19. Take two numbers and print True if at least one is positive.
# 20. Take number and print True if it is between 10 and 20.
# 21. Take marks and print True if marks >= 35 and marks <= 100.
# 22. Take temperature and print True if temperature < 0 or temperature > 40.
# 23. What will be the output?
    
#     print(bool(0))
    
# 24. What will be the output?
    
#     print(bool(1))
    
# 25. What will be the output?
    
#     print(bool(""))
    
# 26. What will be the output?
    
#     print(bool("Hello"))
    
# 27. Take a string input and print True if it equals "admin".
# 28. Take password input and print True if password is not "1234".
# 29. Take a number and print True if it is divisible by 3 and 5.
# 30. Take a number and print True if it is not zero.

# 1. What is a Boolean value in Python?
# Boolean value in Python is a data type that represents only two possible values:

# True
# False

#2.These are used to check conditions and make decisions in a program.
# x = 5 > 3   # True
# y = 5 < 3   # False

# print(x)
# print(y)

# 3.What will be the output?
# print(10 > 5)

# 4. What will be the output?
    
# print(5 == 10)

# 5. What will be the output?
    
# print(5 != 5)

#  6. What is the result of:
    
# print(10 >= 10) 

# 7. What is the result of:
    
# print(3 < 1)
# 
#  8. Take a number and print True if it is positive. 
# num =int(input("Enter a num"))

# if num == 0:
#    print("it is positive")
# else:
#    print(" it is notpositive")   

# 9.Take a number and print True if it is even.
# num = int(input("Enter a numbedr"))
# if num % 2 == 0:
#     print("it is even.")
# else:
#     print("it is  not even.")   
# 
#  10. Take age and print True if age >= 18.
# age = int(input("Enter a age"))
# if age >= 18:
#     print("it is  >= 18")
# else:
#     print("it is not >= 18")    

#  11.What will be the output?
# print(True and False)

# 12. What will be the output?
    
# print(True or False)
# 13. What will be the output?
    
# print(not True)

# 14. What will be the output?
    
# print(not False)

# 15. What will be the output?
    
# print(5 > 2 and 10 > 3)

#  16. What will be the output?
    
# print(5 > 2 and 3 > 10)


# 17. What will be the output?
    
# print(5 > 2 or 3 > 10)

# 18. Take two numbers and print True if both are positive.
# num = int(input("Enter a num:"))
# num1= int(input("Enter a num:"))
# if num % 2 == 0 and num1 % 2 == 0:
#     print(" both are positive ")
# else:
#     print(" both are not positive.")   

#  19. Take two numbers and print True if at least one is positive.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(a > 0 or b > 0)

# 20. Take number and print True if it is between 10 and 20.

# num = int(input("Enter a num:"))
# if num > 10 and num < 20 :
#     print("it is between 10 and 20")
# else:
#     print("it is not between 10 and 20")  
#   
#  21. Take marks and print True if marks >= 35 and marks <= 100.
# marks = int(input("Enter a num:"))
# if marks >= 35 and marks <= 100:
#     print("it is 35 between 100")
# else:
#     print("it is not 35 between 100")    

# 22. Take temperature and print True if temperature < 0 or temperature > 40.
# tem = int(input("Entera tem"))
# if tem < 0 or tem > 40:
#     print(" temperature < 0 or temperature > 40")
# else:
#     print(" temperature is not < 0 or temperature > 40")  
# 
# 23. What will be the output?
    
# print(bool(0)) 
# 
#  24. What will be the output? 
# print(bool(1))
    
# 25. What will be the output?
    
# print(bool(""))
    
# 26. What will be the output?
    
# print(bool("Hello"))

# 27. Take a string input and print True if it equals "admin".
# srt = input("Enter a string")
# if srt == "admin":
#     print("it equals admin")
# else:
#     print("it  is not equals admin")    


# 28. Take password input and print True if password is not "1234".

# password = int(input("Entera  a password"))
# if password != "1234":
#     print("password is not 1234")
# else:
#     print("password is 1234") 


# 29. Take a number and print True if it is divisible by 3 and 5.  
# num = int(input("Enter a num:"))
# if num % 3 == 0 and num % 5 == 0:
#     print("it is divisible by 3 and 5")
# else:
#     print("it is  not divisible by 3 and 5") 
#    
#  30. Take a number and print True if it is not zero.
# num = int(input("Enter a num:"))
# if num != 0:
#     print("it is not zero")
# else:
#     print("it is zero")
