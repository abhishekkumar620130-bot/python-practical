# 1. Take age and check if age > 18 and age < 60.
# 2. Take marks and check if marks >= 35 and marks <= 100.
# 3. Take salary and check if salary > 30000 and experience > 2.
# 4. Take two numbers and check if both are positive.
# 5. Take a number and check if it is between 10 and 50.
# 6. Take username and password and validate both.
# 7. Take age and check if age < 18 or age > 60.
# 8. Take marks and check if marks < 35 or marks > 100.
# 9. Take temperature and check if temp > 40 or temp < 0.
# 10. Take two numbers and check if at least one is negative.
# 11. Take number and check if it is not zero.
# 12. Take age and check if not (age < 18).
# 13. Take a number and check if it is even and greater than 10.
# 14. Take salary and check if salary > 50000 or department == "IT".
# 15. Take two strings and check if both are equal and not empty.
# 16. Take number and check if it is divisible by 3 and 5.
# 17. Take number and check if it is divisible by 3 or 5.
# 18. Take marks and check if marks >= 90 or marks < 40.
# 19. Take password and check if it is not "1234".
# 20. Take two numbers and check if both are not equal to zero.
# 21. Take age and check if age >= 18 and age <= 25.
# 22. Take temperature and check safe range (20–30).
# 23. Take salary and check if salary > 40000 and not salary > 100000.
# 24. Take number and check if not (number > 0).
# 25. Take username and check if username == "admin" or username == "root".
# 26. Take number and check if it is odd and greater than 50.
# 27. Take number and check if it is positive or zero.
# 28. Take marks and check if marks >= 75 and marks < 90.
# 29. Take two inputs and check if both are same and greater than 10.
# 30. Take number and check if it is not between 10 and 20.


# Take age and check if age > 18 and age < 60.

# age = int(input("Enter a age:"))

# if 18 < age < 60:
#     print("age is between 18 and 60.")
# else : print("age is outside the range.")

# 2.2. Take marks and check if marks >= 35 and marks <= 100.

# marks = int(input("Enter a number: "))
# if marks >= 35 and marks <=100:
#    print("result: pass")

# else:
#      print("result: fail or invalid marks")

#

# 3.Take salary and check if salary > 30000 and experience > 2.

# salary = int(input("Enter a number"))
# experience = int(input("Enter a number"))
# if salary > 30000 and experience >2:
#      print("status: eligible for promotion/lone")
# else:
#      print("it is not eligible promotion/lone")  
# 
#  4. Take two numbers and check if both are positive.  

# first = int(input("Enter a number: "))
# second = int(input("Enter a number: "))

# if first > 0 and second > 0:
#      print("result: it is positive number:")
# else:
#      print("result: it is negative number:")

# 5.Take a number and check if it is between 10 and 50.

# num = int(input("enter a number:"))

# if num >= 10 and  num <= 50:
#     print('result: it no long numer')
# else:    
#     print('result: it long number')

# 6. Take username and password and validate both.
# correct_name = "admin"
# correct_password ="123"

# username = input("Enter a username:")
# password = input("Enter password:")
# if username == correct_name and password == correct_password:
#     print("login successful!")
# else:
#     print("login is not successful" )    

# 7. Take age and check if age < 18 or age > 60.

# age = int(input("enter a age:"))
# if age < 18 or age > 60:
#     print("it is eligible:")
# else: 
#     print("it is not eligible:")  
#  
# 8.  8. Take marks and check if marks < 35 or marks > 100.

# marks = int(input("Enter a marks:"))

# if marks < 35 :
#     print("fail condition")
# elif marks > 100 :
#     print("invalid condition")
# else:
#     print("pass and valid marks")    

# 9. Take temperature and check if temp > 40 or temp < 0.

# temperature = int(input("Enter a temperature:"))
# if temperature > 40:
#         print("it very high temperature: ")
# elif temperature < 0:
#         print("it is simple temperature:")
# else:
#         print("it is invlid")   
# 
# 10.   Take two numbers and check if at least one is negative.  
# num = int(input("Enter a number:"))
# num1 = int(input("Enyter a number:"))

# if num < 0 or num1 < 0:
#     print("At least one number is negative")
# else:
#     print("Both number are poaitive ")    
# 11.Take number and check if it is not zero.

# num = int(input("Enter a number:"))
# if num != 0 :
#     print("it is not zero")
# else: 
#     print("it is zero")    


# 12. Take age and check if not (age < 18).

# age = int(input("enter a age:"))
# if age < 18:
#     print("you are audlt. ")
# else:
#     print("it is not audlt.")

# 13.13. Take a number and check if it is even and greater than 10.

# num = int(input("Enter a num:"))
# if num % 2 == 0 and num > 10:
#     print("number even hai aur 10 se bada hai")
# else:
#     ("number nhi bada hai")  

# 14. Take salary and check if salary > 50000 or department == "IT".

# salary = int(input("Enter a salry:"))
# if salary > 50000 or department == "it":
#     print("your salary  is 50000" )
# else:
#     print("your salary is not 50000")  
# 


# num = int(input("Enter a num:"))
# if num %2 == 0:
#     print("Even") 
#     print("squre:",num*num)
# else:
#     print("odd number")    

# 15.  Take two strings and check if both are equal and not empty. 
  
# num = "apple"
# num1 = "banana"

# if num != "" and num1 != "":
#      if num == num1 :
#        print("String are equal and not empty")
#      else:
#        print("string are not equal")
# else:
    #   print("one or both string are empty")    


#  16. Take number and check if it is divisible by 3 and 5.

# num = int(input("Enter a number"))
# if num % 3 == 0 and num % 5 == 0:
#        print("it is divisible")
# else: 
#     print("it is not divisible")


# num = int(input("Enter a number"))
# if num % 3 == 0 and num % 5 == 0:
#       print("it is divisible")
# else:
#       print("it is not divisible")      

# Take marks and check if marks >= 90 or marks < 40.
# marks = int(input("Enter a marks:"))
# if marks >= 90 or  marks < 40 :
#     print("it marks 90 ya big than 90")
# else: 
#     print("it condition is false")  
    
# marks = int(input("Enter a marks"))
# if marks >= 90 or marks < 40:
#     print("it condition true") 
# else:
#     print("it condition is false")    

# 19. Take password and check if it is not "1234".
# password = int(input("Enter a password"))
# if password == 1234:
#        print("it is corret password ")
# else: 
#      print("it is not not corret")

# 20. Take two numbers and check if both are not equal to zero.

# num = int(input("Enter a num:"))
# num2 = int(input("Enter a number:"))
# if num != 0 and num2 != 0:
#   print("it is not zero")
# else:
#   print("it is  zero")   

#  21. Take age and check if age >= 18 and age <= 25.

# age = int(input("Enter a age:"))
# if age >= 18 and age <=25:
#     print("it is perfect age")
# else:
#     print("it is not perfect")    

# 22. Take temperature and check safe range (20–30).
# tem = int(input("Enter tem:"))
# if tem >= 20 and tem <= 30:
#     print("it temperaturen between 20 - 30")
# else:
#     print("it not temperaturen between 20 - 30")   

# 23. Take salary and check if salary > 40000 and not salary > 100000.
# salary = int(input("Enter a salary:"))
# if salary > 40000 and  not salary > 100000:
#     print("salary is  in the required range")
# else:
#     print("salary is not in the required range")    

# 24. Take number and check if not (number > 0).

# num = int(input("Enter a number"))
# if not  num > 0:
#     print("it is not big number")
# else:
#     print("it is big number")    

# 25. Take username and check if username == "admin" or username == "root".
# username = input ("Enter a num:")
# if username == "admin" or username == "root":
#     print("it is correct username")
# else: 
#     print("it is not correct username")    

# 26. Take number and check if it is odd and greater than 50.
# num = int(input ("Enter a num:"))
# if num % 2 != 0 and num > 50:
#     print("it is odd and greter than")
# else:
#     print("it is even num and greter than")    

# 27. Take number and check if it is positive or zero
# num =  int(input("Enter a number:"))
# if num >= 0:
#     print("it is positive number")
# else:
#     print("number is negative")    

# 28. Take marks and check if marks >= 75 and marks < 90.
# marks = int(input("Enter a marks:"))
# if marks >=75 and marks < 90:
#     print("it condition is follow")
# else:
#     print("it is not condition follow")   
# 29. Take two inputs and check if both are same and greater than 10.


# num = int(input("Enter a num "))
# num2 = int(input("Enter a num"))
# if num == num2 and num > 10 :
#     print("Both numbers are same and greater than 10")
# else:
#     print("Both numbers are not same and greater than 10") 
#
# 30.Take number and check if it is not between 10 and 20.

# num = int(input("Enter a num:"))
# if not num <= 10 or num >=20:
#     print("Number is NOT between 10 and 20")
# else:
#     print("number is between 10 and 20") 

# num = int(input("Enter a num"))
# if not num <= 100 or num >= 200:
#     print("it is condition is follow")
# else:
#     print("it is no follow condition")        


   