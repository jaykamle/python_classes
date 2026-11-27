for i in range(1,6):
    print(i)

#example 2

for i in range(5):
    print(i)

#example 3
for i in  range(2,10,2):
    print(i)

#while loop

#example 1

i =1

while i<=5:
    print(i)

    i+=1

#example 2

i=1

while i<=3:
    print("hello")

    i+=1

#infinite Loop
i=1

while i<=5:
    print(i)

#break example

for i in range(1,10):
    if i ==5:

        break
    print(i)

#conitnue (condition ko skkip kardega)

for i in range(1,6):
    if i ==3:
        continue

    print(i)

#pass example

for i in range(1,5):

    if i ==3:
        pass
    print(i)


#COMBINED EXAMPLE OF BREAK/CONTINUE/PASS

for i in range(1,11):

    if i==5:
        continue

    if i==9:
        break

    print(i)

#example:- for loop

for i in range(1,4):


    print(i)

#wxample of whileloop

i=1

while i<=3:

    print(i)

    i+=1


#PRACTICE PROGRAMS

#TABLE PRINT

num =int(input("enter number: "))

for i in range(1,11):

    print(num,"x",i,"=", num*i)


#2. sum of numbers

total =0

for i in range(1,6):
    total +=i

print("total:",total)

#3. WHILELOOP example

i=1

while i<=5:

    print("hello")

    i+=1

#EVEN NUMBERS

for i in range(2,11,2):

    print(i)

#5. skip one number

for i in range (1,6):

    if i ==4:
        continue

    print(i)


