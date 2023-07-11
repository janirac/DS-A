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

# def map_by_key(arr, key):
#     hashes = []
    
#     for item in arr:
#         hashes.append(item[key])
        
#     return hashes

# locations = [
#   {"city": "New York City", "state": "New York", "coast": "East"},
#   {"city": "San Francisco", "state": "California", "coast": "West"},
#   {"city": "Portland", "state": "Oregon", "coast": "West"}
# ]

# print(map_by_key(locations, "state"))

# def yell_sentence(sent):
#     sent_array = sent.split(" ")
#     count = 0
    
#     for sentence in sent_array:
#         sent_array[count] = sentence.upper() + "!"
#         count += 1
        
#     return " ".join(sent_array)
    
# print(yell_sentence("I have a bad feeling about this")) #=> "I! HAVE! A! BAD! FEELING! ABOUT! THIS!"

# def whisper_words(words):
#     new_words = []
    
#     for word in words:
#         new_words.append(word.lower() + "...") 
        
#     return new_words

# print(whisper_words(["KEEP", "The", "NOISE", "down"]))

# def o_words(sentence):
#     arr = []
#     for word in sentence.split(" "):
#         if "o" in word:
#             arr.append(word)
            
#     return arr

# print(o_words("How did you do that?"))

# def last_index(string, char):
#     for i in range(len(string)-1, -1, -1):
#         if string[i] == char:
#             return i
        
# print(last_index("mississipi", "i"))

# def most_vowels(sentence):
#     vowels = "aeiou"
#     most = 0
#     words = ""
    
#     for word in sentence.split(" "):
#         current_count = 0
#         for char in word:
#             if char in vowels:
#                 current_count += 1
#         if current_count > most:
#             most = current_count
#             words = word
            
            
#     return words

# print(most_vowels("what a wonderful life"))


    
# print(prime(2))
# print(prime(5))
# print(prime(11))
# print(prime(4))
# print(prime(9))
# print(prime(-5))

# def pick_primes(array):
#     primes = []
    
#     for num in array:
#         if prime(num):
#             primes.append(num)
            
#     return primes


# print(pick_primes([101, 20, 103, 2017]))

# def prime_factors(num):
#     primes = []
    
#     for i in range(1, num + 1):
#         if num % i == 0 and prime(i):
#             primes.append(i)
            
#     return primes

# def prime(num):
#         if num == 2:
#             return True
        
#         if num < 2:
#             return False
        
#         i = 2
        
#         while i < num:
#             if num % i == 0:
#                 return False
            
#             i += 1
            
#         return True
    
# def prime_factors(num):
    
#     primes = [factor for factor in range(2, num + 1) if num % factor == 0 and prime(factor)]
    
#     return primes

# print(prime_factors(60))

# def find_gcf(num):
#     i = num - 1
#     while i > 0:
#         if num % i == 0:
#             return i
#         i-= 1

# def greatest_factor_array(arr):
#     greatest_array = []
    
#     for num in arr:
#         if num % 2 == 0:
#             greatest_factor = find_gcf(num)
#             greatest_array.append(greatest_factor)
#         else: 
#             greatest_array.append(num)
            
#     return greatest_array            
        
        
# print(greatest_factor_array([16, 7, 9, 14]))

# def perfect_square(num):
#     for factor in range(1, num+1):
#         if factor * factor == num:
#             return True
        
#     return False


# print(perfect_square(25))

# def triple_sequence(start, length):
#     array = [start]
#     count = 0
    
#     while len(array) < length:
#         array.append(array[count] * 3)
#         count += 1
        
#     return array

# print(triple_sequence(4, 5))

def summation_sequence(start, length):
    summations = [start]
    count = 0
    sum = 0
    
    
    while len(summations) < length:
        
        
        for n in range(1, summations[count]):
             sum += n
        
        count += 1
        summations.append(sum)
        
        
    return summations
             
             
             
print(summation_sequence(3, 4))
