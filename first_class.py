#example ; 1

age =20

if age >=18:
    print("adult")

#examplw:2


marks =90
if marks >=40:
    print("pass")

#IF-ELSE STATEMENT

#example:-1
age =15
if age >=18:
    print("adult")
else:
    print("minor")

#EXAMPLE:-2
num =7
if num %2 ==0:
    print("even")
else:
    print("odd")

# ELIF STATEMENT
 
 #EXAMPLE:-1
age =65

if age <18:
    print("minor")
elif age <60:
    print("adult")
else:
    print("senior citizen")

#EXAMPLE:-2

marks =75

if marks >=90:
    print("grade A")
elif marks >=60:
    print("grade B")
elif marks >=40:
    print("pass")
else:
    print("fail")


#COMBINEDD EXAMPLE

marks =75


if marks >=90:
    print("grade A")
elif marks >=60:
    print("grade B")
elif marks >=40:
    print("pass")
else:
    print("fail")



# nested if (extra concept)

age =20
has_id =True

if age >=18:
    if has_id ==True:
        print("entry allowed")

#correct example

age =18

if age ==18:
    print("exactly 18")


#practice programs

#1. EVEN/ODD

num =int(input("enter number:"))

if num %2==0:
    print("even")
else:
    print("odd")


#2. POSITIVE/NEGATIVE/ZERO

num =int(input("enter number:"))


if num >0:
    print("positive")
elif num ==0:
    print("zero")
else:
    print("Negative")



#login cheack

username =input("enter username: ")

if username == "admin":
    print ("login success")
else:
    print("access denied")


#4. largest two numbbers

a=10
b=20

if a>b:
    print("A is greater")

else:
    print("B is greater")


#5. Grade system
marks=88

if marks >=90:
    print("A grade")
elif marks >=75:
    print("B Grade")
elif marks >=40:
    print("pass")
else:
    print("fail")


#END OF MODULE 7




