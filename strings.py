#exxample 1

name ="python"
city ="bhopal"

print(name)
print(city)

#STRING INDEXING EXAMPLE

name ="python"

print(name[0])
print(name[3])

#NEGATIVE INDEXING EXAMPLE

name ="python"

print(name[-1])

#STRING SLICING EXAMPLE

name ="python" 

print(name[0:4])

name ="python"

print(name[3:6])

name ="python"
print(name[:3])

#STRING METHODS

#1.CASE METHODS

text ="hello world"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

#SEARCHING METHODS

text ="hello python"

print(text.find("p"))
print(text.count("o"))
print(text.startswith("h"))
print(text.endswith('n'))

#3.modify methods

text ="hello python"

print(text.strip())
print(text.replace("python","java"))

#4. split &join

text ="I LOVE PYTHON"

words =text.split()
print(words)

new_text="-".join(words)
print(new_text)

#check methods (true/fales)

text ="python123"

print(text.isalpha())
print(text.isalnum())
print(text.isdigit())


#5.f-string(modern way)

name ="python"

print(f"hello {name}")

#example 2(multiple variables)

name ="rahul"
age =25

print(f"my name is {name} and in am {age} years old")

#example 3(expression use)

a =10
b =20

print(f"sum is {a+b}")

#final class demo 

name ="rahul"
text ="hello python"

print(f"hello {name}")
print(text.upper())
print(text.strip())
print(text.replace("python","java"))
print(text.split())