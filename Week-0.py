x = 5

name = "Six Seven\n"

print(x, name )

age = 67

print("Age:", age )

height = 6.7

print("Height:", height )

message = "Blah Blah Blah \n"

print("Message:", message )

is_six_seven = False

print("Is Six Seven:", is_six_seven)

numbers = [1,2,3,4,5,6,7]

print("Numbers : ", numbers )

tupless = (6,7,8,9)

print("Tupless : ", tupless)

dictionary = {"Name":"Rathod", "USN":163}

print("dictionary : ",dictionary);

sum = 6+7

print("Sum:", sum)

difference = 7-6

print("Difference:", difference)

product = 6 * 7

print("Product:", product)

quotient = 201/3

print("Quotient:", quotient)

remainder = 21%5

print("Remainder:", remainder)

power = 3 ** 3

print("Power:", power)

is_equal = (123 == 123)

print("Is Equal:", is_equal)

is_greater = (1000 > 576)

print("Is Greater:", is_greater)

is_less_or_equal = (7 <= 20)

print("Is Less or Equal:", is_less_or_equal)

and_result = (True and False)

print("AND Result:", and_result)

or_result = (True or False)

print("OR Result:", or_result)

not_result = (not True)

print("NOT Result:", not_result)

my_list = [10,20,30,'yokoso','watashi no ','soul','society']

print("My_List : ",my_list)

my_list[3]=3

print("MOdified List :",my_list)

my_list.append('Bankai')

print("List with added element:", my_list)

my_list.remove(10)

print("List with removed element:", my_list)



x = 10

if x > 5:
    print("x is greater than 5")

elif x == 5:
    print("x is equal to 5")

else:
    print("x is less than 5")



numbers = [5,10,15,20,25]

for num in numbers:
    print(num)


x = 2

while x < 20:
    print(x)
    x += 2


num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)


def fun(name):
    print(name)
    
fun("Rathod")
