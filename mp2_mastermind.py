"""
Student Name: Julian Navarro 
Date: October 9, 2022

Brief program overview (2-3 senteces)
This program is the game Mastemind. The game creates a secret code for the codebreaker to decipher in the
least amount of tries. The code is 4 characters long and it is composed of the characters 'B', 'W', 'R', 'G', 'Y' and 'O'.
After the codebreaker gives tries the game will return how close the player is with his guess by giving a 'b' for 
correct position of the character, 'w' correct letter in the code but in wrong position and '-' for incorrect letter. 
When the code is cracked the game will share with the player in how many moves it was cracked. 
"""
import random 


def make_random_code():
    """
    This function takes no argument and returns of exaclty four characters randomnize.

    Paramenters:
        none 

    Returns:
        (string) - A string of four characters out of 'B', 'W', 'R', 'G', 'Y' and 'O'
    """
    string = ""
    colors = ["R", "G", "B", "Y", "O", "W"]
    for x in range (4):
        string += random.choice(colors)
    return string 


def count_exact_matches(first_str, second_str):
    """
    Given two string 'first_str' and 'second_str', returns the number of places in which the strings 
    have the exact same lettters and position.

    Parameters:
        'first_str' and 'second_str' (str) - Four letter strings that are going to be compared. 
    Returns:
        (integer) - Returns the number of places where the two string ('first_str' and 'second_str')
        have the exact same letters at the exact same position.
    """
    count = 0 
    for i in range(len(first_str)): 
        if first_str[i] == second_str[i]:
            count += 1
    return count


def count_letter_matches(first_str, second_str):
    """
    Given two string 'first_str' and 'second_str', returns the number of letters of the two strings
    that are the same no matter the order. 

    Paramenters:
        'first_str' and 'second_str' (str) - Four letter strings that are going to be compared. 

    Returns:
        (integer) - Returns the number of letters of the two string ('first_str' and 'second_str') 
        that are the same regardless of order. 
    """
    count = 0
    lst_first_str = list(first_str)
    lst_second_str = list(second_str)
    for lst in lst_first_str:
        if lst in lst_second_str:
            count += 1
            lst_second_str.remove(lst)
    return count

                
def compare_codes(code, guess):
    """
    Given a 'code' and a 'guess', returns the key pegs of the similarity between 'code' and 'guess'. 

    Parameters:
        'code' and 'guess' (str) - These are four letters strings that are the secret code and the guess
        of the player or codebreaker respectevely. 

    Returns:
        (string) - Returns a string of lenght 4 consisting of the characters 'b', 'w' and '-', meeaning the pegs
        that the codebreaker did. 
    """
    number_of_b = count_exact_matches(code, guess) 
    number_of_w = count_letter_matches(code, guess) - number_of_b
    number_of_dashes = 4 - number_of_b - number_of_w
    return number_of_b * "b" + number_of_w * "w" + number_of_dashes * "-"

def run_game():
    """
    This function runs the game Mastermind. It will ask for the codebreaker's guess and it will print the result
    given in the fucntion 'compare_codes'. If codebreaker crackes the code it will print a 'congratulations' with 
    the amount of tries it took the codebreaker to crack the code. 
    Paramenters: 
        none

    Returns:
        (string) - Returns the result and if you cracked the code it returns a congratulations and the number
        of moves you cracked it. 
    """
    print("New game.")
    secret_code = make_random_code()
    moves = 0
    while True: 
        guess = input("Enter your guess: ")
        compare = compare_codes(secret_code, guess)
        print("Result: " + compare)
        moves += 1
        if compare == "bbbb":
            print("Congratulations! You cracked the code in " + moves + "moves!")
            break 
            
if __name__ == '__main__':
    run_game()