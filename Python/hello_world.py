# print('Hello World') #can write a string like this "" or ''

# age = 20
# age = 30
# age = "I am a string now"
# age = False


# first_name = "John"
# last_name = "Smith"
# age = 20
# new_patient = True

# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input("Enter your birth year: ")
# age = 2023 - int(birth_year)
# print(age)

# first_number = input("First: ")
# second_number = input("Second: ")
# print("Sum: " + str(float(first_number) + float(second_number)))

# print(age)

# course = "Python for Beginners"
# new_course = course.isdigit()
# print('Python' in course) #returns a boolean if the given str in found where as using the find will return the index
# print(new_course)
# print(course)

# x = (10 + 3) * 2
# x = 3 == 3
# print(x)

# price = 5

# print( not price > 10)

# temperature = 5

# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else: 
#     print("It's cold")
# print("Done")

# weight = float(input("Weight: "))
# unit = input("(K)g or (L)bs: ").lower()
# if unit == "l":
#     print("Weight in kg: " + str(weight * 0.45))
# else:
#     print("Weight in kg: " + str(weight))
    

# i = 1

# while i < 10:
#     print(i * '*')
#     i+=1

# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# names[0] = "Jon"
# print(names[0:3])
# print(names)

# numbers = [1,2,3,4,5]

# print(numbers)

# for item in numbers:
#     print(item)
    
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# numbers = range(5, 10, 2)
# for number in numbers:
#     print(number)

# numbers = (1, 2, 3)
# print(numbers.count(3))

# find the longest common prefix
# iterate over the strs array
# create a variable that keeps track of the current prefix
# Check each element to see if it has that prefix keep going until the first length is finished
# if its not there take off the end of the current prefix


# def longest_common_prefix(strs): 
#     if not strs:                  
#         return "NONE"

#     prefix = strs[0]
#     for string in strs:
#         while not string.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
            
#     return prefix


# strs = []
# print(longest_common_prefix(strs))

# def map_by_name(arr):
#     hashes = []
    
#     for hash in arr:
#         hashes.append(hash["name"])
        
#     return hashes

# pets = [
#   {"type": "dog", "name": "Rolo"},
#   {"type": "cat", "name": "Sunny"},
#   {"type": "rat", "name": "Saki"},
#   {"type": "dog", "name": "Finn"},
#   {"type": "cat", "name": "Buffy"}
# ]

# print(map_by_name(pets))

def map_by_key(arr, key):
    hashes = []
    
    for item in arr:
        hashes.append(item[key])
        
    return hashes

locations = [
  {"city": "New York City", "state": "New York", "coast": "East"},
  {"city": "San Francisco", "state": "California", "coast": "West"},
  {"city": "Portland", "state": "Oregon", "coast": "West"}
]

print(map_by_key(locations, "state"))