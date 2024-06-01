
class Lab2:

    def __init__(self) :

        self.greeting = "Hello this is LAB 02"

# Write a Python program that takes a user input of a temperature in Celsius and 
# converts it to Fahrenheit using variables and arithmetic operations.
    
    def celciusToFarenheit(self,celcius):

        farenheit = (9/5) * celcius + 32
        return farenheit

# Create a for loop that iterates through a list of numbers and prints out only the even 
# numbers.Write a Python program that uses a loop variable to calculate the sum of 
# the first 100 numbers.

    def getEvenAndSum(self, nums):

        print("The even numbers in the list are : ",end=" ")
        for num in nums:

            if num % 2 == 0:

                print(str(num),end=" ")
        
        sum = 0

        for i in range(1,101):

            sum = sum + i
        
        print("\nThe sum of first 100 numbers is " + str(sum),end=" ")

# Create a function that takes a list of numbers and returns the maximum and 
# minimum values in the list.
    def minAndMax(self,arr):

        return min(arr) ,max(arr)

# Write a Python program that takes a user input of a string and prints out whether the 
# string is a palindrome or not using if statements.

    def checkPalindrome(self,word):

        rev = word[::-1]

        if word == rev:
            return True
        else:
            return False

# Create a program that uses a flag variable to determine if a user input of a number is 
# prime or not.
            
    def checkPrime(self,num):

        if num <= 1:
            return "The number is not prime"

        if num == 2:
            return "The number is prime"

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return "The number is not prime"

        return "The number is prime"
    
# Write a Python program that sorts a list of numbers in ascending order without using 
# the built-in sort() method.
    
    def sortList(self, arr):

        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


        

# Create a function that takes two strings as input and returns True if the second string 
# is a substring of the first string, and False otherwise.

    def checkSubstring(self,str1,str2):
        return str2 in str1

# Write a Python program that uses indexing to replace the first occurrence of a 
# character in a string with another character.

    def replaceCharacter (self,strx,oldChar,newChar):
        for i in range(len(strx)):
            if strx[i] == oldChar:
                strx = strx[:i] + newChar + strx[i+1:]
                break  
        return strx

# Create a program that takes a user input of a list of strings and prints out the length 
# of each string.

    def printLenOfString (self,arrOfStrings):
        for word in arrOfStrings:

            print("The Length of " + word + " is : ",str(len(word)))

lab2 = Lab2()

print(lab2.greeting)

celcius = float(input("Enter temprature in celcius : "))

farenheit = lab2.celciusToFarenheit(celcius)

print(str(farenheit))

arr = [1,2,34,6,67,43,332,4,3,4]
lab2.getEvenAndSum(arr)

print("\nThe minimum and maximum in the list is : "+str(lab2.minAndMax(arr)))

print("Is Palindrome : " + str(lab2.checkPalindrome("abc")))

print(lab2.checkPrime(3))


numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = lab2.sortList(numbers)
print("Sorted list:", sorted_numbers)

print(lab2.checkSubstring('Abdur Rahman',"xyz"))

print(lab2.replaceCharacter("Hello","l","n"))

arrOfWords = ["Abdur","Rahman","Is","an","IT enthusiast"]

lab2.printLenOfString(arrOfWords)