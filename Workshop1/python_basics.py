"""
MDST Workshop 1 - Python Basics Starter Code
"""
import random
import base64
import sys
# Add any imports you need here:


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    #print("Give me a number: ")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    num = random.randint(1, 9)

    while(1):
        val = input("Guess a number: ")
        if int(val) == num:
            print("Exactly right!")
            break
        elif int(val) < num:
            print("Oof! Your guess was too low! Try Again!")
        elif str(val) == "exit":
            break
        else:
            print("Oof! Your guess was too high! Try again")
        

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    sentence = input("Give me a string: ")
    for i in range(len(sentence)):
        if sentence[i] != sentence[(len(sentence)-i-1)]:
            print("False")
            break
    print("True")



def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    file = open(filename, "wb")

    username_bytes = username.encode('ascii')
    encryptedusername = base64.b64encode(username_bytes)
    password_bytes = password.encode('ascii')
    encryptedpassword = base64.b64encode(password_bytes)

    file.write(encryptedusername)
    file.write(encryptedpassword)
    
    file.close()
    


def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    file = open(filename, "r")
    line = list(file)

    for x in line:
        message = base64.b64decode(x)
        base64_message = message.decode('ascii')
        print(base64_message)
    file.close()
    if password != None:
        file = open(filename, "w")
        line[1] = password




if __name__ == "__main__":
    # part1(3)  # odd!
    # part1(4)  # even!
    # part2()
    # part3("ratrace")  # False
    # part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
