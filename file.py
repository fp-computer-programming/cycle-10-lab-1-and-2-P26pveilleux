#Create a Python file named lab_10-1.py
#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Using a while loop, write a program that prompts the user to input a number.
#If the user inputs a number, add that to the sum of the previous numbers entered.
#If the user enters -1, the program should end and display the sum of all the numbers entered.
#Be sure the program uses a break statement
#_____________________________________________________________________________________________________________
num = 1 

while 1:
    s = int(input("number"))
    if s == -1:
        print(num)
        break
    else:
        num += s
#Create a Python file named lab_10-2.py
#Using the same approach as lab 1, write a program that prints all the numbers that are multiples of 3 in a list. Be sure your program uses a continue statemen
num = []
while 1:
    num = input("num:")
    if num == -1:
        return num 
    elif not (s % 3):
        continue
    num += s 
