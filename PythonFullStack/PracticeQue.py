
#Check whether a number is positive , negative or  zero

# num =int(input("Enter num: "))

# if num>0:
#     print("number is positive")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is 0")

#Check whether a number is even or odd

# num1 =int(input("enter number to check: "))

# if num1%2==0:
#     print("number is even")
# else:
#     print("number is odd")


#Check if a number is divisible by both 3 and 5

# num3 =int(input("Enter number to check: "))

# if num3%3==0 and num3%5==0:
#     print("yes, number is divisible by both numbers")
# elif num3%3==0:
#     print("number is only divisible by 3")
# elif num3%5==0:
#     print("number is only divisible by 5")
# else:
#     print("no, number is not divisible by any one")


#Find the largest of the three numbers

# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))

# if(a>=b and a>=c):
#     print("a is largest among three")
# elif(b>=a and b>=c):
#     print("b is largest among three")
# else:
#     print("c is largest among three")



#Check vowel or consonant

# ch =input("enter character value: ")
# if(ch=='a' or ch =='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' ):
#     print("character is vowel")
# else:
#     print("character is consonant")


# cha =input("character to check: ")
# if cha in "aeiouAEIOU":
#   print("vowel")
# else:
#   print("consonant")


#Check if the number is greater than 10 and less than 50

# number =int(input("enter number to check: "))
# if(number>=10 and number<=50):
#  print("number is between 10 and 50")
# else:
#    print("number is out of bound")

# attend=int(input("provide your  aggregate attendence: "))

# if (attend>75):
#     print("yor are eligible to seat for placement")
# elif(attend==75):
#     print("Contact to TPC cell")
# else:
#     print("not eligible to seat in placement")





# userinput=int(input("enter user input: "))

# if  0<userinput<=99:
#     print("valid digit")
# else:
#     print("invalid input")


#Vulnerable Calculator  
# eval()==>used for evaluation ==> __import__("os").system('dir')=>it prints the directory files in the terminal
 
# exp =input("data for eval: ")

# result = eval(exp)

# print(f"The result is {result}")

#Check whether a year is a leap year or not==> a year is divible by 400 OR (divisible by 4 and not by 100)

# year =int(input("Enter year to check leap year: "))

# if(year%400==0) or (year%4==0 and year%100!=0):
#     print(year, ": is a leap year")
# else:
#     print(year, ": is not a leap year")

#Check Temperature Classification

# temp =int(input("enter current temp: "))

# if 10<=temp<=15:
#     print("cold season")
# elif 15<temp<=30:
#     print("moderate season")
# elif temp>30:
#     print("hot season")
# else:
#     print("cannot be determined ")

#Simple Login System
#=> user ='admin' password='password'

# user =str(input("enter user: "))

# password=input("enter password: ")

# if user=='admin' and password =='password':
#     print("user is authorised")
# else:
#     print("unauthorised user")



#Valid triangle

# side1 =int(input("enter side1: "))
# side2 =int(input("enter side2: "))
# side3 =int(input("enter side3: "))

# if (side1 + side2 > side3 and side1 +side3 >side3 and side3+side2>side1):
#     print("triangle formation is valid")
# else:
#     print("invalid condition for triangle formation")

#check if triangle is right-angled

# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))

# if a*a + b*b ==c*c or a*a + c*c ==b*b or b*b + c*c==a*a:
#     print("right-angled triagle")
# else:
#     print("not a right-angled triangle")

    #check the type of triangle
s1 =int(input('enter side s1: '))
s2 =int(input("enter side s2: "))
s3 =int(input("enter side s3: "))
if s1==s2 or s1==s3 or s2==s3:
    print("isosceles triangle")
elif s1 ==s2 and s2==s3:
    print("equilateral triangle")
else:
    print("scalene triangle")



