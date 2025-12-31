#For loop example
for i in range(1, 5):
    print(i)

#While loop example
i = 1
while i <= 5:
    print(i)
    i += 1

#Break statement
for i in range(1, 5):
    if i == 3:
        break
    print(i)

#Continue statement
for i in range(1, 5):
    if i == 3:
        continue
    print(i)

#If Else example
a = 50
b = 100

if a < b:
    print("Yes, a is less than b")
elif a > b:
    print("No, a is not greater than b")

#Boolean value example
logged_in = False

if logged_in:
    print("Log in successful")
else:
    print("Log in unsuccessful")
