#3.1
fav_foods = ["pretzel", "che", "duck", "jackfruit", "cupcake"]
print(fav_foods[1])
print(fav_foods[-1])
fav_foods.append("banh mi")
fav_foods.insert(0, "apple")
fav_foods.remove("duck")
print(len(fav_foods))
for foods in fav_foods:
    print(foods.upper())
    """
    I encountered the error 
    <built-in method upper of str object at 0x00000261275EF2D0>
    I originally wrote: print(foods.upper)
    and i fixed it by putting: print(foods.upper())
    """
new_foods = fav_foods[0:6:5]

if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!")

#3.2
numbers = []
i = 0
for i in range(21):
    numbers.append(i)
    i += 1
print(numbers)

def get_first_15(numbers):
    return numbers[0:15:1]

def get_every_5th(numbers):
    return numbers[0:15:5]

def reverse_and_stride(numbers):
    reversedlist = numbers[::-1]
    return reversedlist[::-3]

step1 =get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)

"""
A problem I had was with getting the different lists to be used within each other
It inputed [0, 1, 2]
I originally had it say step2 = get_every_5th(numbers)
                        step3 = reverse_and_stride(numbers)
I fixed it by putting step2 = get_every_5th(step1)
                            step3 = reverse_and_stride(step2)
                            """


#3.3.1

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(list):
    total = []
    for item in list:
        x =sum(item)
        total.append(x)
        
    totalsum = sum(total)
    return totalsum
        


#3.4
print("3.4 division line")
list = []
def nested_5_by_5(list):
    for i in range(5):
        list.append([])
        for j in range(5):
            num = i*5 + j + 1
            list[i].append(num)
    return list
        

by5x5 = nested_5_by_5(list)

def replace_multiples_of_three(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] % 3 == 0:
                list[i][j] = "?"
                
            
    return list

list_with_question = replace_multiples_of_three(by5x5)
print(list_with_question)

def adding_list_not_question(list):
    total = 0
    for x in list:
        for y in x:
            if y != "?":
                total += y
        
    return total


total_without_multiples_of_three = adding_list_not_question(list_with_question)
            

#4.1

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages.update({"Milana": 52})
del ages["Mariam"]
for name, age in ages.items():
    print(f"{name}: {age}")

"""
I encountered the error 
    ValueError: too many values to unpack (expected 2)
    I originally wrote: for name, age in ages:
    and i fixed it by putting: for name, age in ages.items():
"""


#Favorite function
test_list = [
    [1, 4, 5],
    [4, 6, 9],
    [9, 3, 2],
]

print(sum_nested(test_list))