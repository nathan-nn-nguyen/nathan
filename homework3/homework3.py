#3.1
def say_goodbye(name):
    print("Goodbye,", name)

#say_goodbye("Siena")

#3.2
def circle_area(radius):
    print(radius * radius * 3.14)

#circle_area(2)

#4.1
def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

#print(subtract(1, 2))
#print(multiply(1, 2))
#print(divide(1, 2))

#5.1
def highs_and_lows(temperature):
    maxtemp = max(temperature)
    mintemp = min(temperature)
    return (maxtemp, mintemp)

#temperature = [20, 30, 40, 50]
#print(highs_and_lows(temperature))

#5.2
def is_weekend(day):
    if day == 1:
        return ("Monday")
    if day == 2:
        return ("Tuesday")
    if day == 3:
        return ("Wednesday")
    if day == 4:
        return ("Thursday")
    if day == 5:
        return ("Friday")
    if day == 6:
        return ("Saturday")
    if day == 7:
        return ("Sunday")
    else:
        return ("That's not a day of the week!")

#print(is_weekend(4))

#5.3
def fuel_efficency(distance, fuel):
    return distance / fuel

#print(fuel_efficency(20, 3))

#5.4

def encrypt_data(number):
    import math
    string3 = str(number)
    length_string = len(string3)
    number2 = number % 10
    number3 = number // 10
    return number3 + number2*math.pow(10, length_string - 1)

#print(encrypt_data(8967))

#6.1
def square(x, y):
    xinit = x
    for i in range(y - 1):
        x = x * xinit
    return x

#print(square(6, 3))

#6.2
#6.2.1
def new_min(list_numbers):
    minimum = list_numbers[0]
    for item in list_numbers[1:]:
        if item < minimum:
            minimum = item
    return minimum

#print(new_min(temperature))

def new_max(list_numbers):
    maximum = list_numbers[0]
    for item in list_numbers[1:]:
        if item > maximum:
            maximum = item
    return maximum

#print(new_max(temperature))

#6.2.2
def return_min(list_numbers):
    minimum = list_numbers[0]
    index = 0
    while index < len(list_numbers):
        if minimum > list_numbers[index]:
            minimum = list_numbers[index]
        index +=1
    return minimum

def return_max(list_numbers):
    maximum = list_numbers[0]
    index = 0
    while index < len(list_numbers):
        if maximum < list_numbers[index]:
            maximum = list_numbers[index]
        index +=1
    return maximum
        
#print(return_min(temperature))
#print(return_max(temperature))

#6.3
def new_sum(integer):
    if integer == 0:
        return 0
    else:
        return integer % 10 + new_sum(integer // 10)

#print(new_sum(631))
    

#favorite function- encrypt_data
x = 12345
result = encrypt_data(x)

print(f"The result of encrypt_data (5.4) with x = 12345 is", result)