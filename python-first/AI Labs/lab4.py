
class Lab4:

    def __init__(self) :

        self.greeting = "This is lab four"

#  Create a program that reads from a text file and creates a dictionary where the keys 
# are the words in the file and the values are the number of times each word appears.
    def readFile(self,nameOfFile):
        word_count = {}

        with open(nameOfFile, 'r') as file:
            for line in file:
                words = line.split()

                for word in words:
                    word = word.strip('.,!?:;"\'').lower()
                    
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        return word_count


# Write a function that takes a list of integers and returns the sum of all the even 
# numbers in the list.
    def sumOfAllEven(self,arr):

        sumEven = 0
        for num in arr:
            if num % 2 == 0:
                sumEven = sumEven + num
        
        return sumEven



# • Write a function that takes a list of strings and returns a new list with all the strings
# in upper case.
    def convertToUpperCase(self, arr):

        arr2 = []

        for strx in arr:

            arr2.append(strx.upper())

        return arr2

# • Write a function that takes a list of dictionaries and sorts the list based on the value 
# of a specified key in each dictionary. 
    def sort_dict_list(self,dict_list, key):

        return sorted(dict_list, key=lambda x: x[key])


# • Write a function that takes two lists and returns a new list that contains only the 
# common elements between the two lists.
    def commonElements(self,list1,list2):
        return list(set(list1) & set(list2))



# • Write a function that takes a dictionary as input and returns a new dictionary that 
# contains only the key-value pairs where the value is an integer.
    def checkIntValues(self,input_dict):
        filtered_dict = {}
        for key, value in input_dict.items():
            if isinstance(value, int):
                filtered_dict[key] = value

        return filtered_dict




# • Write a function that takes a dictionary and a string as input and returns a new 
# dictionary that contains only the key-value pairs where the key contains the 
# specified string. 

    def checkStringInDict(self,input_dict,word):

        new_dict = {}

        for key,value in input_dict.items():

            if word == value:
                new_dict[key] = word
        
        return new_dict


# • Write a function that takes two dictionaries and merges them into a single 
# dictionary, where the values for overlapping keys are added together. 
    def mergeTwoDict(self,dict1,dict2):

        mergedDict = {}

        for key,value in dict1.items():
                mergedDict[key] = value + dict2.get(key,0)
        
        for key, value in dict2.items():

            if key not in dict1:
                mergedDict[key] = value 

        return mergedDict
            

# • Write a function that takes a string as input and returns a new string that contains 
# only the vowels in the original string, in the order they appear. 
    def stringContainVowels(self,input_string):
        
        vowels = "aeiouAEIOU"

        result = ""
        for ch in input_string:

            if ch in vowels:
                result += ch
        
        return result
# • Write a function that takes a string as input and returns a new string that is the 
# reverse of the original string.
    def reverseString(self,input_string):

        return input_string[::-1]




lab4 = Lab4()

listOfStrings = ["abc","def","ghi","jkl"]
listOfStrings1 = ["abc","fed","bad","jkl","abc"]

listOfInts = [1,2,3,4,6,5,4,21,3]

print("The sum of all Evens : " + str(lab4.sumOfAllEven(listOfInts)))
print("The List in Uppercase : "+str(lab4.convertToUpperCase(listOfStrings)))
print("The List of Common Elements : "+str(lab4.commonElements(listOfStrings,listOfStrings1)))
print("The Vowels in a string : "+str(lab4.stringContainVowels("aehamzaiou")))
print("The reverse of the string is : "+str(lab4.reverseString("Hamza")))

filename = "dummy.txt"

numOfWords = lab4.readFile(filename)

print("The number of words in the file are : ")

print(str(numOfWords))

dict_list = [
    {'name': 'Hamza', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

sorted_by_age = lab4.sort_dict_list(dict_list, 'age')
print("Sorted by age:")
print(sorted_by_age)

sorted_by_name = lab4.sort_dict_list(dict_list, 'name')
print("\nSorted by name:")
print(sorted_by_name)

sorted_by_city = lab4.sort_dict_list(dict_list, 'city')
print("\nSorted by city:")
print(sorted_by_city)



checkIntValuesDict = {
    'name': 'Hamza',
    'age': 30,
    'city': 'New York'
}
print("\n")
filtered_dict = lab4.checkIntValues(checkIntValuesDict)
print(filtered_dict)


checkwordDistionary = {
    'a': 'Hamza',
    'b': 'New York',
    'c': 'New York'
}

new_dict = lab4.checkStringInDict(checkwordDistionary,"New York")

print(new_dict)


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged_dict = lab4.mergeTwoDict(dict1, dict2)
print(merged_dict)
