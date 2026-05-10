# ### Basic Level (1–15)
# Conditionals
# 1. Take a number and check if it is positive, negative, or zero.
# 2. Take a number and check if it is even or odd.
# 3. Take age and print:
#     - "Child" if age < 13
#     - "Teen" if age 13–19
#     - "Adult" otherwise
# 4. Take marks and print:
#     - "Fail" if < 35
#     - "Pass" if 35–59
#     - "First Class" if 60–79
#     - "Distinction" if 80+
# 5. Take temperature and print:
#     - "Cold" if < 15
#     - "Warm" if 15–30
#     - "Hot" if > 30
# 6. Take salary and classify:
#     - Low (< 30000)
#     - Medium (30000–70000)
#     - High (> 70000)
# 7. Take a number and check if it is divisible by 3, 5, or both.
# 8. Take two numbers and print which one is greater or if equal.
# 9. Take a character and check if it is a vowel or consonant.
# 10. Take a year and check if it is leap year or not.
# 11. Take a number and check if it is 1-digit, 2-digit, or 3-digit.
# 12. Take exam score and print grade (A, B, C, D, F).
# 13. Take a number and check if it lies between 10 and 50.
# 14. Take username and check:
#     - "admin" → Admin Access
#     - "guest" → Guest Access
#     - otherwise → Invalid User
# 15. Take password and check if it matches "python123".

# ---

# ### Intermediate Level (16–35)

# 1. Take three numbers and print the largest.
# 2. Take three numbers and print the smallest.
# 3. Take a number and check if it is divisible by 2 and 3.
# 4. Take number and print:
#     - "Small" if < 10
#     - "Medium" if 10–100
#     - "Large" if > 100
# 5. Take income and calculate tax:
#     - < 2.5L → No tax
#     - 2.5L–5L → 5%
#     - 5L–10L → 10%
#     - 10L → 20%
# 6. Take two numbers and check if one is multiple of another.
# 7. Take a string and check:
#     - If length < 5 → Short
#     - 5–10 → Medium
#     - 10 → Long
# 8. Take age and check voting eligibility (>=18).
# 9. Take electricity units and calculate bill based on slab.
# 10. Take basic salary and calculate bonus based on experience.
# 11. Take a number and check if it is a perfect square.
# 12. Take day number (1–7) and print weekday name.
# 13. Take month number (1–12) and print month name.
# 14. Take a number and classify as:
#     - Even positive
#     - Even negative
#     - Odd positive
#     - Odd negative
# 15. Take two strings and check if they are equal ignoring case.
# 16. Take a float number and check if it is integer value or decimal.
# 17. Take percentage and check scholarship eligibility.
# 18. Take two numbers and check if they form a right triangle (Pythagoras).
# 19. Take speed and classify:
#     - Slow (< 30)
#     - Normal (30–70)
#     - Fast (> 70)
# 20. Take login attempts and print warning after 3 attempts.

# ---

# ### Advanced Logic Practice (36–50)

# 1. Take a number and print:
#     - "Fizz" if divisible by 3
#     - "Buzz" if divisible by 5
#     - "FizzBuzz" if divisible by both
#     - otherwise print number
# 2. Take age and gender and check special ticket discount eligibility.
# 3. Take salary and experience and classify promotion eligibility.
# 4. Take two numbers and check if both are positive, both negative, or mixed.
# 5. Take number and check if it lies in:
#     - 0–50
#     - 51–100
#     - 101–200
#     - above 200
# 6. Take character input and check:
#     - uppercase
#     - lowercase
#     - digit
#     - special character
# 7. Take three sides and check:
#     - Equilateral
#     - Isosceles
#     - Scalene triangle
# 8. Take a number and check Armstrong number (3-digit).
# 9. Take balance and withdrawal amount. Check if transaction is allowed.
# 10. Take score and print performance message.
# 11. Take age and check insurance premium category.
# 12. Take two numbers and check if they are both even, both odd, or mixed.
# 13. Take time in hours and print:
#     - Morning
#     - Afternoon
#     - Evening
#     - Night
# 14. Take product price and customer type (regular/premium) and calculate discount.
# 15. Take a number and check:
#     - Less than 0
#     - Between 0 and 100
#     - Greater than 100
#     - Exactly 100

# Hard questions

## HARD LEVEL NESTED IF-ELIF-ELSE QUESTIONS

# 1. Take age and citizenship.
    
#     If age >= 18:
    
#     If citizenship is "Indian" → Eligible to vote
    
#     Else → Not eligible (citizenship issue)
    
#     Else → Not eligible (age issue)
    
# 2. Take marks in 3 subjects.
    
#     If all marks >= 35:
    
#     Calculate average:
    
#     If average >= 75 → Distinction
    
#     If 60–74 → First Class
    
#     Else → Pass
    
#     Else → Fail
    
# 3. Take salary and experience.
    
#     If salary > 50000:
    
#     If experience >= 5 → Promotion eligible
    
#     Else → Not eligible (experience low)
    
#     Else → Salary too low
    
# 4. Take username and password.
    
#     If username == "admin":
    
#     If password == "1234":
    
#     Login successful
    
#     Else:
    
#     Wrong password
    
#     Else:
    
#     Invalid username
    
# 5. Take a number.
    
#     If number > 0:
    
#     If number % 2 == 0:
    
#     If number % 4 == 0 → Divisible by 4
    
#     Else → Even but not divisible by 4
    
#     Else → Odd positive
    
#     Else:
    
#     Negative or zero
    
# 6. Take temperature.
    
#     If temp < 0:
    
#     If temp < -10 → Extreme cold
    
#     Else → Freezing
    
#     Else:
    
#     If temp <= 30 → Normal
    
#     Else → Hot
    
# 7. Take income and age.
    
#     If income > 300000:
    
#     If age < 60 → Tax applicable
    
#     Else → Senior citizen discount
    
#     Else → No tax
    
# 8. Take marks and attendance %.
    
#     If attendance >= 75:
    
#     If marks >= 40 → Pass
    
#     Else → Fail (low marks)
    
#     Else → Not eligible for exam
    
# 9. Take 3 sides of triangle.
    
#     If all sides > 0:
    
#     If a+b>c and b+c>a and a+c>b:
    
#     If all equal → Equilateral
    
#     If any two equal → Isosceles
    
#     Else → Scalene
    
#     Else → Not valid triangle
    
#     Else → Invalid input
    
# 10. Take bank balance and withdrawal amount.
    
#     If withdrawal <= balance:
    
#     If withdrawal <= 20000 → Transaction approved
    
#     Else → Limit exceeded
    
#     Else → Insufficient balance
    
# 11. Take two numbers.
    
#     If first > second:
    
#     If first % second == 0 → Divisible
    
#     Else → Not divisible
    
#     Else:
    
#     Reverse logic and check
    
# 12. Take electricity units.
    
#     If units <= 100:
    
#     Low bill
    
#     Else:
    
#     If units <= 300:
    
#     Medium bill
    
#     Else:
    
#     High bill
    
# 13. Take age and driving test score.
    
#     If age >= 18:
    
#     If score >= 80 → License approved
    
#     Else → Retest required
    
#     Else → Not eligible
    
# 14. Take password length and content.
    
#     If length >= 8:
    
#     If contains digit:
    
#     If contains uppercase:
    
#     Strong password
    
#     Else → Medium
    
#     Else → Weak
    
#     Else → Too short
    
# 15. Take product price and customer type.
    
#     If customer == "premium":
    
#     If price > 5000 → 20% discount
    
#     Else → 10% discount
    
#     Else:
    
#     If price > 5000 → 5% discount
    
#     Else → No discount
    
# 16. Take age and health condition.
    
#     If age > 60:
    
#     If health == "good" → Low premium
    
#     Else → High premium
    
#     Else:
    
#     Normal premium
    
# 17. Take exam score.
    
#     If score >= 90:
    
#     Grade A
    
#     Else:
    
#     If score >= 75:
    
#     Grade B
    
#     Else:
    
#     If score >= 50:
    
#     Grade C
    
#     Else:
    
#     Fail
    
# 18. Take time (24-hour format).
    
#     If 0 <= time <= 23:
    
#     If time < 12 → Morning
    
#     Else:
    
#     If time < 17 → Afternoon
    
#     Else:
    
#     If time < 20 → Evening
    
#     Else → Night
    
#     Else → Invalid time
    
# 19. Take number.
    
#     If number != 0:
    
#     If number > 0:
    
#     If number < 100 → Small positive
    
#     Else → Large positive
    
#     Else:
    
#     If number > -100 → Small negative
    
#     Else → Large negative
    
#     Else → Zero
    
# 20. Take username and role.
    
#     If username exists:
    
#     If role == "admin":
    
#     Full access
    
#     Else:
    
#     If role == "editor":
    
#     Edit access
    
#     Else:
    
#     View only
    
#     Else → User not found
    
# 21. Take salary and department.
    
#     If department == "IT":
    
#     If salary > 100000 → Senior Developer
    
#     Else → Junior Developer
    
#     Else:
    
#     If department == "HR":
    
#     HR Staff
    
#     Else:
    
#     Other Department
    
# 22. Take two numbers and check quadrant logic (like coordinates).
    
#     If x > 0:
    
#     If y > 0 → Quadrant 1
    
#     Else → Quadrant 4
    
#     Else:
    
#     If y > 0 → Quadrant 2
    
#     Else → Quadrant 3
    
# 23. Take 3 numbers and check if strictly increasing.
    
#     If a < b:
    
#     If b < c → Strictly increasing
    
#     Else → Not increasing
    
#     Else → Not increasing
    
# 24. Take student type and marks.
    
#     If student == "regular":
    
#     If marks >= 40 → Pass
    
#     Else → Fail
    
#     Else:
    
#     If marks >= 50 → Pass
    
#     Else → Fail
    
# 25. Take number.
    
#     If number % 2 == 0:
    
#     If number % 3 == 0:
    
#     Divisible by 6
    
#     Else:
    
#     Only divisible by 2
    
#     Else:
    
#     If number % 3 == 0:
    
#     Only divisible by 3
    
#     Else:
    
#     Not divisible by 2 or 3
    
# 26. Take credit score.
    
#     If score >= 750:
    
#     Excellent
    
#     Else:
    
#     If score >= 600:
    
#     Average
    
#     Else:
    
#     Poor
    
# 27. Take BMI value.
    
#     If BMI < 18.5:
    
#     Underweight
    
#     Else:
    
#     If BMI < 25:
    
#     Normal
    
#     Else:
    
#     If BMI < 30:
    
#     Overweight
    
#     Else:
    
#     Obese
    
# 28. Take account type and balance.
    
#     If type == "savings":
    
#     If balance >= 1000 → Active
    
#     Else → Below minimum
    
#     Else:
    
#     If type == "current":
    
#     Always active
    
#     Else:
    
#     Invalid type
    
# 29. Take order amount and location.
    
#     If amount > 1000:
    
#     If location == "local":
    
#     Free delivery
    
#     Else:
    
#     Delivery charge applied
    
#     Else:
    
#     No free delivery
    
# 30. Take performance rating and experience.
    
#     If rating >= 4:
    
#     If experience >= 5:
    
#     Promotion + Bonus
    
#     Else:
    
#     Bonus only
    
#     Else:
    
#     If rating >= 3:
    
#     No promotion
    
#     Else:
    
#     Performance improvement required


# 1. Take a number and check if it is positive, negative, or zero.
# num = float(input("Enter a num:"))
# if num > 0 :
#     print("it is positive")
# elif num < 0:
#     print("it is  negative")
# else:
#     print("it is zero")   
#
# 2. Take a number and check if it is even or odd.
# num = int(input("Enter a num:"))
# if num % 2 == 0 :
#     print(" it is even")
# else:
#     # print("it is even or odd") 
# 
# 
# 3. Take age and print:
#     - "Child" if age < 13
#     - "Teen" if age 13–19
#     - "Adult" otherwise 

# age = int(input("Enter a age:"))
# if age  < 13 :
#     print("it is child")  
# elif age > 13 and age < 19:
#     print(" it is teen")
# else:
#     print("it is adult")   
# 
# 4. Take marks and print:
#     - "Fail" if < 35
#     - "Pass" if 35–59
#     - "First Class" if 60–79
#     - "Distinction" if 80+ 


# marks = int(input("Enter a marks:"))
# if marks < 35:
#     print("fail")
# elif marks >= 35 and marks <= 59:
#     print("pass")
# elif marks >= 60 and marks <=79:
#     print("First Class")    
# else:
#     print("Distinction") 


#  5.Take temperature and print:
#     - "Cold" if < 15
#     - "Warm" if 15–30
#     - "Hot" if > 30


# tem = int(input("Enter a tem"))
# if tem < 15:
#     print("it is cold")
# elif tem >= 15 and tem <= 30:
#     print("warm")
# elif tem > 30:
#      print("hot") 
# 
#  6. Take salary and classify:
#     - Low (< 30000)
#     - Medium (30000–70000)
#     - High (> 70000)
# 
# salary = int(input("Enter a salary"))
# if salary < 30000:
#     print("low")
# elif salary >= 30000 and salary <=70000:
#     print("it is medium")  
# elif salary > 70000:
#     print("it is high")  
# 
#  8. Take a number and check Armstrong number (3-digit).

# 9.Take two numbers and print which one is greater or if equal.
#
#  num = int(input("Enter a num:"))
# num2 = int(input("Enter a num:"))  

# if num < num2:
#     print(num2, "is greater")
# elif num > num2:
#     print(num,"is greater")  
# else:
#     print("both are equla")    
# 
# 9. Take a character and check if it is a vowel or consonant.
# ch = input("Enter a char")
# if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#     print("it is a vowel")
# else:
#     print("it is a consonant")    

# 10. Take a year and check if it is leap year or not.
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# 11. Take a number and check if it is a perfect square.

# num = int(input("Enter a num:"))
# root = int(num ** 0.5)
# if root * root == num:
#     print("perfect squre")
# else:
#     ("not a perfect squre")

#
# 
# 14. Take username and check:
#     - "admin" → Admin Access
#     - "guest" → Guest Access
#     - otherwise → Invalid User
#

# 11. Take a number and check if it is 1-digit, 2-digit, or 3-digit.
# num = int(input("Enter a num:"))
# if num < 1:
#     print("it is  1-digit")
# elif  num < 10:
#     print("it is 2-digit")  
# elif num < 100:
#     print("it is 3-digit") 
# 
#  12. Take exam score and print grade (A, B, C, D, F).
# score = input("Enter a num:")
# if score == "A":
#     print("it is A")
# elif score == "B":
#     print("it is B")
# elif score == "c":
#     print("it is c")
# elif score == "D"  :
#     print("it is F")     

# 13. Take a number and check if it lies between 10 and 50.
# num = int(input("Enter a num:"))
# if num >=10 and num <= 50:
#     print(" it lies between 10 and 50")
# else:
#     print(" it lies  not between 10 and 50.")   
#  

# 14. Take username and check:
#     - "admin" → Admin Access
#     - "guest" → Guest Access
#     - otherwise → Invalid User

# username = input("Enter a username")
# if username == "admin":
#     print(" Admin Access")
# elif username == "guest":
#     print("Guest access")
# else:
#     print("it is invalid user")   
#   
#  15. Take password and check if it matches "python123".
# password = input("Enter a password")
# if password == "python123":
#         print("it is correct")
# else:
#         print("it is not correct")     
#    


# Hard questions

## HARD LEVEL NESTED IF-ELIF-ELSE QUESTIONS

# 1. Take age and citizenship.
    
#     If age >= 18:
    
#     If citizenship is "Indian" → Eligible to vote
    
#     Else → Not eligible (citizenship issue)
    
#     Else → Not eligible (age issue)

# answer -:
# age = int(input("Enter a age: "))
# citizenship = input("Enter a citizenship: ")

# if age >= 18:
#     if citizenship == "Indian":
#         print("Eligible to vote")
#     else:
#         print("Not eligible (citizenship issue)")
# else:
#     print("Not eligible (age issue)")

#  2. Take marks in 3 subjects.
    
#     If all marks >= 35:
    
#     Calculate average:
    
#     If average >= 75 → Distinction
    
#     If 60–74 → First Class
    
#     Else → Pass
    
#     Else → Fail


# m1 = int(input("Enter marks"))
# m2 = int(input("Enter marks"))
# m3 = int(input("Enter marks"))

# if m1 >= 35 and m2 >= 35 and m3 >= 35:

#     average = (m1 + m2 + m3) / 3

#     if average >= 75:
#         print("Distinction")

#     elif average >= 60 and average <= 74:
#         print("First Class")

#     else:
#         print("Pass")

# else:
#     print("Fail")

#  3. Take salary and experience.
    
#     If salary > 50000:
    
#     If experience >= 5 → Promotion eligible
    
#     Else → Not eligible (experience low)
    
#     Else → Salary too low

# salary = int(input("Enter a salary:"))
# experience = int(input("Enter a experince:"))
# if salary > 5000:
#     if experience >= 5:
#         print("it is Promotion eligible") 
#     else:
#             print("Not eligible (experience low)")
# else:
#             print("Salary too low")         


# 4. Take username and password.
    
#     If username == "admin":
    
#     If password == "1234":
    
#     Login successful
    
#     Else:
    
#     Wrong password
    
#     Else:
    
#     Invalid username
 

# username = input("Enter a name:")
# password = input("Enter a password")
# if username == "admin" :
#     if password == "1234":
#      print("Login successful")
#     else:
#         print("Wrong password") 
# else:
#          print("Invalid username")     
#   
# 5. Take a number.
    
#     If number > 0:
    
#     If number % 2 == 0:
    
#     If number % 4 == 0 → Divisible by 4
    
#     Else → Even but not divisible by 4
    
#     Else → Odd positive
    
#     Else:
    
#     Negative or zero

# num = int(input("Enter a num:"))
# if num > 0 :
#     if num % 2 ==0:
#      if num % 4 == 0:
#         print("Divisible by 4")
#      else:
#        print("Even but not divisible by 4")
#     else:
#        print("Odd positive")
    
# else:
#       print(" Negative or zero")

# 6. Take temperature.
    
#     If temp < 0:
    
#     If temp < -10 → Extreme cold
    
#     Else → Freezing
    
#     Else:
    
#     If temp <= 30 → Normal
    
#     Else → Hot
    
# tem = int(input("ENter a tem: "))
# if tem < 0:
#     if tem <-10:
#         print("Extreme cold")
#     else:
#           print("Freezing")
# else:
#    if tem <= 30:
#            print("Normal")   
#    else:
#      print("hot")        
          
    #  7. Take income and age.
    
#     If income > 300000:
    
#     If age < 60 → Tax applicable
    
#     Else → Senior citizen discount
    
#     Else → No tax    
# 
# income = int(input("Enter a income")) 
# if income > 300000:
#     if age < 60:
#      print("Tax applicable")
#     else:
#      print("Senior citizen discount")
# else:
#     print("No tax  ")

# 8. Take marks and attendance %.
    
#     If attendance >= 75:
    
#     If marks >= 40 → Pass
    
#     Else → Fail (low marks)
    
#     Else → Not eligible for exam

# marks = int(input("Enter a marks:"))
# att = int(input("Enter a att:"))
# if att >= 75:
#     if marks >= 40:
#       print("pass") 
#     else:
#      print("fail")
# else:
#     print("Not eligible for exam")  
#  
#  9. Take 3 sides of triangle.
    
#     If all sides > 0:
    
#     If a+b>c and b+c>a and a+c>b:
    
#     If all equal → Equilateral
    
#     If any two equal → Isosceles
    
#     Else → Scalene
    
#     Else → Not valid triangle
    
#     Else → Invalid input

# a = int(input("Enter side a: "))
# b = int(input("Enter side b: "))
# c = int(input("Enter side c:"))
# if a > 0 and b > 0 and c > 0:
#      if a+b+c and b+c>a and a+c>b:
#          if a == b and b == c:
#              print("Equilateral")
#          elif a == b and b==c:
#           print("Isosceles")
#          else:
#           print("Scalene") 
#      else:  
#        print("Not valid triangle")   
# else:
#      print("Invalid input")  

#  10. Take bank balance and withdrawal amount.
    
#     If withdrawal <= balance:
    
#     If withdrawal <= 20000 → Transaction approved
    
#     Else → Limit exceeded
    
#     Else → Insufficient balance

# balance = int(input("Enter a balance:"))
# withdrawal = int(input("Entera withdrawal: "))
# if withdrawal <= balance:
#     if withdrawal <= 20000:
#         print("Transaction approved") 
#     else:
#         print("Limit exceeded")    
# else:
#     print("Insufficient balance")  
# 
# 11. Take two numbers.
    
#     If first > second:
    
#     If first % second == 0 → Divisible
    
#     Else → Not divisible
    
#     Else:
    
#     Reverse logic and check 

# num = int(input("Enter a num:"))
# num1 = int(input("Enter a num:"))
# if num > num1:
#     if num % num1 ==0:
#         print("Divisible")
#     else:
#         print("Not divisible")    
# else:
#     print("Reverse logic and check")

# 12. Take electricity units.
    
#     If units <= 100:
    
#     Low bill
    
#     Else:
    
#     If units <= 300:
    
#     Medium bill
    
#     Else:
    
#     High bill
# units = int(input("Enter a units:"))
# if unit <= 100:
#     print("Low bill")
# else:
#     if units <= 300:
#         print("Medium bill")
#     else:
#         print("high bill")


# 13. Take age and driving test score.
    
#     If age >= 18:
    
#     If score >= 80 → License approved
    
#     Else → Retest required
    
#     Else → Not eligible/

# age = int(input("Enter a age:"))
# score = int(input("Enter a score:"))
# if age >= 18:
#     if score >= 80:
#      print("License approved") 
#     else:
#      print("Retest required")   
# else:
#   print("Not eligible")
#  
# 
# 14. Take password length and content.
    
#     If length >= 8:
    
#     If contains digit:
    
#     If contains uppercase:
    
#     Strong password
    
#     Else → Medium
    
#     Else → Weak
    
#     Else → Too short  


# password = input("Enter password: ")

# if len(password) >= 8:

#     if any(ch.isdigit() for ch in password):

#         if any(ch.isupper() for ch in password):
#             print("Strong password")

#         else:
#             print("Medium")

#     else:
#         print("Weak")

# else:
#     print("Too short")

# 15. Take product price and customer type.
    
#     If customer == "premium":
    
#     If price > 5000 → 20% discount
    
#     Else → 10% discount
    
#     Else:
    
#     If price > 5000 → 5% discount
    
#     Else → No discount

# price = float(input("Enter product price:"))
# customer = input("Enter customer type :")
# if customer == "premium":
#     if price > 5000:
#         discount = price * 0.20
#         print("discount", discount)
#     else:
#         discount = price * 0.10
#         print("discount=", discount)

# 16. Take age and health condition.
    
#     If age > 60:
    
#     If health == "good" → Low premium
    
#     Else → High premium
    
#     Else:
    
#     Normal premium

# age = int(input("Enter age:"))
# health = input("Enter health condition (good/poor):")
# if age > 60:
#    if health == "good":
#        print("low premium")
#    else:
#        print("high premium")
# else:
#     print("normal premium")

   
# 17. Take exam score.
    
#     If score >= 90:
    
#     Grade A
    
#     Else:
    
#     If score >= 75:
    
#     Grade B
    
#     Else:
    
#     If score >= 50:
    
#     Grade C
    
#     Else:
    
#     Fail

# score = int(input("Enter exam score:"))
# if score >= 90:
#     print("grade A")
# else:
#     if score >= 75:
#         print("grade b")
#     else:
#         if score >= 50:
#             print("grade c")
#         else:
#             print("fail")


# 18. Take time (24-hour format).
    
#     If 0 <= time <= 23:
    
#     If time < 12 → Morning
    
#     Else:
    
#     If time < 17 → Afternoon
    
#     Else:
    
#     If time < 20 → Evening
    
#     Else → Night
    
#     Else → Invalid time
    
# time = int(input("Enter time (0-23):"))
# if time <= 23 and time >= 0:
#     if time < 12:
#      print("morning")
#     else:
#        if time < 17 :
#         print("afternoon") 
#        else:
#          if time < 20:
#            print("Evening")
#          else:
#            print("night")
# else:
#             print("invalid time")

# 20. Take username and role.
    
#     If username exists:
    
#     If role == "admin":
    
#     Full access
    
#     Else:
    
#     If role == "editor":
    
#     Edit access
    
#     Else:
    
#     View only
    
#     Else → User not found
# username = input("Enter username:")
# role = input("Enter  a role: ")
# if username :
#     if role == "admin":
#         print("full access")
#     else:
#         if rple == "editior":
#             print("edit access")
#         else:
#             print("view only")

# 21. Take salary and department.
    
#     If department == "IT":
    
#     If salary > 100000 → Senior Developer
    
#     Else → Junior Developer
    
#     Else:
    
#     If department == "HR":
    
#     HR Staff
    
#     Else:
    
#     Other Department

# salary = int(input("Enter salary:"))
# dep = input("Enter department:")
# if dep == "it":
#     if salary > 100000:
#         print("Senior developer")
#     else:
#       print("junior developer")
    
# elif dep == "HR": 
#        print("HR staff")
# else:
#     print("other department")

    # 22. Take two numbers and check quadrant logic (like coordinates).
    
#     If x > 0:
    
#     If y > 0 → Quadrant 1
    
#     Else → Quadrant 4
    
#     Else:
    
#     If y > 0 → Quadrant 2
    
#     Else → Quadrant 3  
  
# x = int(input("Enter x coordinate:"))
# y = int(input("Enter y coordinate:"))
# if x > 0:
#     if y > 0:
#         print("Quadrant 1")
#     else:
#         print("quadrant 4")
    
# elif y > 0:
#      print("Quadrant 2")
# else:
#         print("Quadrant 3")

# 23. Take 3 numbers and check if strictly increasing.
    
#     If a < b:
    
#     If b < c → Strictly increasing
    
#     Else → Not increasing
    
#     Else → Not increasing
# a = int(input("Enter a :"))
# b = int(input("Enter b :"))
# c = int(input("Enter c:"))
# if a < b:
#     if b < c:
#         print("strictly increasing")
#     else:
#         print("not increasing")
# else:
#     print("not increasing")

# 24. Take student type and marks.
    
#     If student == "regular":
    
#     If marks >= 40 → Pass
    
#     Else → F ail
    
#     Else:
    
#     If marks >= 50 → Pass
    
#     Else → Fail

# student = input("Enter student type (regular/special)")
# marks = int(input("Enter marks:"))
# if student == "regular":
#     if marks >= 40:
#         print("pass")
#     else:
#         print("fail")
    
# elif marks >= 50:
#       print("pass")
# else:
#         print("fail")

# 25. Take number.
    
#     If number % 2 == 0:
    
#     If number % 3 == 0:
    
#     Divisible by 6
    
#     Else:
    
#     Only divisible by 2
    
#     Else:
    
#     If number % 3 == 0:
    
#     Only divisible by 3
    
#     Else:
    
#     Not divisible by 2 or 3

# num = int(input("Enter a num:"))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("divisible by 6")
#     else:
#         print("only divisible by 2")
# elif num % 3 == 0:
#     print("only divisible by 3")
# else:
#     print("not divisible by 2 or 3")        


#  26. Take credit score.
    
#     If score >= 750:
    
#     Excellent
    
#     Else:
    
#     If score >= 600:
    
#     Average
    
#     Else:
    
#     Poor

# score = int(input("Enter credit score:"))
# if score >= 750:
#     print("Excellent")
# elif score >= 600:
#         print("Average")
# else:
#         print("poor")


#