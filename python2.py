# KWK-python-review

python review for data science from KWK
x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)

Karlie = "Karlie"
also_Karlie = "Karlie"

print("Karlie == Karlie: ", Karlie == Karlie)
print("Karlie == also_Karlie", Karlie == also_Karlie)

firstName = "Layla"
age = 15

print ("Layla == Karlie : ", firstName == Karlie)
print ("Age == 16 : ", age == 16)
print("Age != 16 : ", age != 16)
print("Age > 8 : ",age > 8)
print("Age <= 10 : ", age <= 10)
print(age % 2)

a = 100
b = 200

if b > a:
  print("b is greater than a")

# an if statement that determines if b > a

a=50
b=50

if b > a: 
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# use elif to see if a = b

a=100
b=50

if b > a: 
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# use else to see if b > a


lucky_number = 19

if lucky_number < 50:
  print("Nice! Your lucky number is less than 50")
else:
  print("Your lucky number is not less than 50")
  
  print((9 > 7) and (2 < 4))  # Both original expressions are True
print((8 == 8) or (6 != 6)) # One original expression is True
print(not(3 <= 1))          # The original expression is False

a = 200
b = 100
c = 500
if a > b and c > a:
  print("both conditions are true")
  
  a = 200
b = 100
c = 500
if a > b or a > c:
  print("at least one of the conditions is true")
  
  favoriteFood = "Pizza"

if favoriteFood == "Chipotle":
  print("your favorite food is Chipotle")
elif favoriteFood == "Starbucks":
  print("your favorite food is Starbucks")
elif favoriteFood == ""

# create a while loop that print the numbers 1-5 

i = 1
while i < 6:
  print(i)
  i += 1
  
  x = [1]
while x[-1] <= 100:
  x.append(sum(x))

print(x)

# create a for loop to print:
fruits = ["apple", "banana", "cherry"]
for item in fruits:
  print(item)
  
  # demonstrating a basic for-loop
total = 0
for item in [1, 3, 5]:
    total = total + item
 
print(total)
# `total` has the value 1 + 3 + 5 = 9
# `item` is still defined here, and holds the value 5

alphabet = "abcdefghij"
for letter in alphabet:
  if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(letter)
    
    # Use of break statement inside the loop
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

for val in "string":
    if val == "i":
        continue
    print(val)

    
    #Create a sequence of numbers from 0 to 5, and print each item in the sequence:
x = range(6)
for n in x:
  print(n)
for val in range(16):
    if val%3 == 0 and val%5 == 0:
      print("fizzbuzz")
      continue   
    elif val%3 == 0:
        print("fizz")
        continue
    elif val%5 == 0:
      print("buzz")
      continue
    
    print(val)
  
