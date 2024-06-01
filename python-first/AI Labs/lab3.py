import random


class Lab3:

    def __init__(self) :

        self.greeting = "This is lab three"


# Create a program that takes a user input of a list of strings and prints out the 
# length of each string.
    def lenOfStringsInAList(self,input_string_list):

        for word in input_string_list:

            print("The len of the "+word + " is :"+ str(len(word)))



# • Write a Python program that uses list comprehensions to create a list of all the 
# prime numbers less than or equal to a user input.
    
    def isPrime(self,n):

        if n<= 1:
            return False
        if n == 2:
            return True
        
        for i in range(2,n-1):

            if n % i == 0:
                return False
        
        return True
    def primeListUpToN(self,N):

        primeList = []

        for i in range(1,N) :

            if self.isPrime(i):
                primeList.append(i)
        
        return primeList

# • Create a two-dimensional list that represents a tic-tac-toe board and write a 
# function that checks if either player has won. 
    def print_board(self,board):
        for row in board:
            print('|'.join(row))
            print('-' * 5)

    def check_winner(self,board):
        # Check rows for a win
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return f"Player {row[0]} wins!"

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                return f"Player {board[0][col]} wins!"

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return f"Player {board[0][0]} wins!"
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return f"Player {board[0][2]} wins!"

        return None

    def check_draw(self,board):
        for row in board:
            if ' ' in row:
                return False
        return True

    def play_game(self):
        current_player = 'X'
        while True:
            self.print_board(tic_tac_toe_board)
            print(f"Player {current_player}'s turn")

            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))

            if tic_tac_toe_board[row][col] == ' ':
                tic_tac_toe_board[row][col] = current_player
            else:
                print("Cell already taken. Try again.")
                continue

            winner = self.check_winner(tic_tac_toe_board)
            if winner:
                self.print_board(tic_tac_toe_board)
                print(winner)
                break

            if self.check_draw(tic_tac_toe_board):
                self.print_board(tic_tac_toe_board)
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'



    # • Write a program that uses the random module to simulate rolling two dice and 
    # calculates the probability of rolling a double.
    def rollDice(self):
            return random.randint(1,6),random.randint(1,6)
    def findProbability(self,numberOfRolls):

            sameDoubleCount = 0

            for _ in range(numberOfRolls):

                dice1,dice2 = self.rollDice()

                if dice1 == dice2 :
                    sameDoubleCount += 1
                
            return sameDoubleCount/numberOfRolls


    # • Create a function that takes a sentence as input and uses the split() and join() 
    # methods to reverse the order of the words in the sentence. 

    def reverseSentence (self,sentence):

            word = sentence.split()
            reverse_order = word[::-1]

            reversed_sentence = ' '.join(reverse_order)

            return reversed_sentence


    # • Write a program that uses short-circuiting to find the first non-zero value in a 
    # list of numbers. 
    def checkFirstNonZero(self,input_list) :

            for num in input_list:
                if num != 0:

                    return num
            return


    # • Create a function that uses continuation to find the sum of all the even 
    # numbers between 1 and a user input. 
    def findSumTillN (self, N):

            sumOfEvens = 0
            for i in range(0,N + 1):

                if i % 2 == 0:

                    sumOfEvens = sumOfEvens+i
            
            return sumOfEvens
        
    # • Write a Python program that uses pass statements to create a skeleton class 
    # for a bank account with withdraw and deposit methods.
    def performBankOperations(self,initial_balance,withdrawAmount,depositAmount):
            account = BankAccount(initial_balance)
            account.withdraw(withdrawAmount)
            account.deposit(depositAmount)



    # • Create a program that uses string formatting to print out a multiplication table 
    # for all the numbers between 1 and 10. 
    def tablesWithFormating(self):

            print("   |",end="")
            for i in range(1,10+1):
                print(f"{i:2}",end=" ")
            print()
            print("---*" + "---" * 10,end="")
            print()
            for i in range(1,11):
                print(f"{i:2} |",end="")
                for j in range(1,11):
                    result = i * j
                    print(f" {result:2}", end="")
                print()
            


    # • Write a Python program that uses dictionaries to keep track of the number of 
    # times each word appears in a sentence.
    def checkTheNumberOfTimesOfWordInSen(self,sentence):

            wordsDict = {}
            words = sentence.split()
            for word in words:
                if word in wordsDict:
                    wordsDict[word] +=1
                else:
                    wordsDict[word] = 1
            
            return wordsDict

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal failed. Insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit failed. Invalid amount.")

lab3 = Lab3()

print(lab3.greeting)

input_string_list = ["Abdur Rahman","Wasif Ullah","Muhammad Mubashir","Muhammad Maaz","Shahid Alam"]
lab3.lenOfStringsInAList(input_string_list)


print(str(lab3.primeListUpToN(200)))


numberOfRolls = 50000

probabilityOfSameDouble = lab3.findProbability(numberOfRolls)

print("The probability of getting the double is : "+str(probabilityOfSameDouble))


input_sentence = "Hello This is Abdur Rahman , How are you Abdur Rahman ? "

reverseSentence = lab3.reverseSentence(input_sentence)

print(reverseSentence)


numbersOrCurrents = [0,0,0,0,9,1,0,0,0]

print("This is the FIrst NonZero: " + str(lab3.checkFirstNonZero(numbersOrCurrents)))


N = 12

print("The sum of all Even till " + str(N) + " is : "+str(lab3.findSumTillN(N)))

lab3.tablesWithFormating()


print(lab3.checkTheNumberOfTimesOfWordInSen(input_sentence))

initail_balance = 50000

withdrawAmount = 10000

depositAmount = 20000

lab3.performBankOperations(initail_balance,withdrawAmount,depositAmount)



tic_tac_toe_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

lab3.play_game()



