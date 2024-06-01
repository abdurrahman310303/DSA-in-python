# All Rights are Reserved By ABDUR RAHMAN and can be justified...
import string

class Lab1:

    def __init__(self):
        self.greeting = "This is Lab one"

# Write a Python function that takes in a list of integers as an argument and returns the 
# sum of all the elements in the list.

    def sumOfAllInList(self, arr):
        return sum(arr)

# Write a Python function that takes in a list of integers as an argument and returns the 
# largest element in the list.

    def largestInArr(self, arr):
        return max(arr)

# Write a Python function that takes in a dictionary as an argument and returns a new 
# dictionary that contains only the key-value pairs where the key is a string and the value is 
# an integer

    def separateKeyValue(self, input_dict):
        result = {}
        for k, v in input_dict.items():
            if isinstance(k, str) and isinstance(v, int):
                result[k] = v
        return result

# Write a Python function that takes in a list of integers as an argument and returns a new 
# list that contains only the even integers from the input list.

    def getEvensFromList(self, arr):
        return [num for num in arr if num % 2 == 0]

# Python function that takes in a list of integers as an argument and returns a new list that 
# contains the elements of the input list in reverse order

    def reverseList(self, arr):
        return arr[::-1]

# Write a simple program in dictionary that takes value from user and also sum and 
# subtract these values and then print it.

    def get_user_values(self):
        values_dict = {}
        num_values = int(input("Enter the number of values: "))
        for i in range(num_values):
            key = input(f"Enter key for value {i + 1}: ")
            value = int(input(f"Enter integer value for {key}: "))
            values_dict[key] = value
        return values_dict

    def sum_values(self, values_dict):
        return sum(values_dict.values())

    def subtract_values(self, values_dict):
        values = list(values_dict.values())
        result = values[0]
        for value in values[1:]:
            result -= value
        return result

# Write a program in dictionary which uses ‘in’ operator and copy methods in python.And 
# why we use ‘in’ operator.

    def useOfIN(self, listx):
        print("This program is for the use of 'in' in Python")
        for num in listx:
            print(num)

# Write a Python function that takes in a dictionary as an argument and returns a new 
# dictionary that contains the same key-value pairs as the input dictionary, but with all the 
# values converted to lowercase.

    def getAndConvertToLower(self, input_dict):
        lower_dict = {}
        for key, value in input_dict.items():
            if isinstance(value, str):
                lower_dict[key] = value.lower()
            else:
                lower_dict[key] = value
        return lower_dict

# Write a Python function that takes in a dictionary as an argument and returns a new 
# dictionary that contains the same key-value pairs as the input dictionary, but with all the 
# values sorted in ascending order.

    def sort_dict_values(self, input_dict):
        sorted_dict = {}
        for key, value in input_dict.items():
            if isinstance(value, list):
                if all(isinstance(item, int) for item in value):
                    sorted_dict[key] = sorted(value)
                else:
                    sorted_dict[key] = value
            else:
                sorted_dict[key] = value
        return sorted_dict

# Write a Python function that takes in a list of strings as an argument and returns a new 
# list that contains the same strings as the input list, but with all punctuation characters 
# removed.

    def remove_punctuation(self, strings_list):
        translation_table = str.maketrans('', '', string.punctuation)
        cleaned_list = [s.translate(translation_table) for s in strings_list]
        return cleaned_list

lab1 = Lab1()

nums = [1, 2, 3, 5]
print(str(lab1.sumOfAllInList(nums)))
print(str(lab1.largestInArr(nums)))

input_dict = {
    'a': 1,
    'b': 2.5,
    'c': 3,
    4: 'd',
    'e': 'f',
    'g': 7
}
print(str(lab1.separateKeyValue(input_dict)))

print(str(lab1.getEvensFromList(nums)))
print(str(lab1.reverseList(nums)))

user_values = lab1.get_user_values()
sum_result = lab1.sum_values(user_values)
subtract_result = lab1.subtract_values(user_values)
print("Dictionary of user values:", user_values)
print("Sum of all values:", sum_result)
print("Result of subtracting all values:", subtract_result)

x_dict = {
    'a': "ABD",
    'b': "BDC",
    'c': "Djfd",
    "d": 'ddjlakjfd',
    'e': 'ffjakld',
    'g': "fjkadDDD1"
}
print(lab1.getAndConvertToLower(x_dict))

toSort = {
    "numbers": [5, 3, 1, 4, 2],
    "letters": ["b", "d", "a", "c"],
    "name": "Alice",
    "mixed": [3, "a", 2, "b"]
}
sorted_dict = lab1.sort_dict_values(toSort)
print("The sorted Dictionariy is : ",end=" ")
print(sorted_dict)

strings_list = ["Hello, World!", "Python is awesome!", "How are you?"]
cleaned_list = lab1.remove_punctuation(strings_list)
print(cleaned_list)
