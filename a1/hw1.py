"""
Student Name: Julian Navarro 
Date: October 4, 2022

HW1
"""
# Exercise A: Course Policies
# A.1 - not allowed
# A.2 - allowed
# A.3 - allowed
# A.4 - not allowed
# A.5 - allowed
# A.6 - not allowed
# A.7 - allowed
# A.8 - not allowed
# A.9 - not allowed 

# Exercise B.1: Expressions
# Ex B.1.1: 8-5 --> 3
# Ex B.1.2: 6 * 2.5 --> 15.0
# Ex B.1.3: 51 / 2 --> 25.5
# Ex B.1.4: 51 / -2 --> -25.5
# Ex B.1.5: 51 % 2 --> 1
# Ex B.1.6: 51 % -2 --> -1
# Ex B.1.7: -51 % 2 --> 1
# Ex B.1.8: 51 / -2.0 --> -25.5
# Ex B.1.9: 1 + 4 * 5 --> 21
# Ex B.1.10: (1 + 4) * 5 --> 25

# Exercise B.2: Shortcut Expressions
# Ex B.2.1: x = 120 --> 120
# Ex B.2.2: x = x + 10 --> 130
# Ex B.2.3: x += 20 --> 150 
# Ex B.2.4: x = x - 30 -->120
# Ex. B.2.5: x -= 70 --> 50
# Ex B.2.6: x *= 3 --> 150
# Ex. B.2.7: x /= 5 --> 30.0  
# Ex. B.2.8: x %= 5 --> 0.0

#Exercise B.3: Evaluation walkthrough
# Ex B.3: 
# 1. Rewrite x += x - x to x = x + (x - x). 
# 2. Lookup the variable x to get its initial value x-> 3.
# 3. x after the statement has been evaluated is replaced with its value 3 
# 4. x = x + (x - x) ->  x = 3 + (3 - 3)
# 5. Now evaluate (3 - 3) first due to order of operations -> 0.
#    x = 3 +(0)
# 6. Now evaluate 3 + (0) -> 3
#    x = 3
# 7. Re-assing x to 3 


#Exercise B.4: Complex numbers
# Ex B.4.1: 1j + 2.4j --> 3.4j
# Ex B.4.2: 4j * 4j --> (-16 + 0j)
# Ex B.4.3: (1+2j) / (3+4j) --> (0.44+0.08j)
# Ex B.4.4: (1+2j) * (1+2j) --> (-3+4j)
# Ex B.4.5: 1+2j * 1+2j --> (1+4j)
# Ex B.4.6: The answers are different because Python undestands the PENDAS order of operation. In problem B.4.4 it 
# does first the parenthesis and then the multiplication. In problem B.4.5 it does first the multiplication and then 
# the addition because there is no parenthesis. Python considers complex numbers as different type than real numbers. 
# It regocnizes that you cannot sum real and complex numbers and have to leave them expressed. 

#Exercise B.5: Functions on complex numbers 
# Ex B.5.1: cmath.sin(-1.0+2.0j) --> (-3.165778513216168+1.959601041421606j)
# Ex B.5.2: cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)
# Ex B.5.3: cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)
# Ex B.5.4: It is better to write 'import math' and 'import cmath' because  using 'from math import*' calls 
# every module from  math and cmath and it can cause confusion and causes names to overlap with other imports


#Exercise B.6: String expressions 
# Ex B.6.1: "foo" + 'bar'--> 'foobar'
# Ex B.6.2: "foo" 'bar' --> 'foobar'
# Ex B.6.3: a = 'foo' \n b = "bar" \n a + b --> 'foobar'
# Ex B.6.4: a = 'foo' \n b = "bar" \n a b --> File "<stdin>", line 1
#                                           a b
#                                             ^
#                                     SyntaxError: invalid syntax

# Ex B.6.5: month = "October" \n days = 31 \n days + " days hath " + month # --> Traceback (most recent call last):
#                                                                            File "<stdin>", line 1, in <module>                                                          
#                                                                          TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Exercise B.7: Fun with quotes 
# Ex B.7 -->'A\nB\nC'

#Exercise B.8: String generation 
# Ex B.8: --> '-' * 70

#Exercise B.9: A string puzzle
# Ex B.9: --> print("Line 1\nLine 2\nLine 3")

#Exercise B.10: String formatting  
x = 9
y = 4.25
# Ex B.10.1:
print("Lorem is {}.".format(x))
# Ex B.10.2:
print("Lorem is {} months old.".format(x))
# Ex B.10.3:
print( "A puppuccino is ${}.".format(y))
# Ex B.10.4:
print( "{} * {}".format(y,x))
# Ex B.10.5:
print( "{} * {} is {}.".format(y, x, y * x)) 

# Exercise B.11: Terminal input
num = float(input("Enter a number: "))
print(num)

# Exercise B.12: Quadratic expressions
def quadratic(a, b, c, x):
    """
    Function takes 4 inputs a, b, c and x. Computes and returns the value
    of the quadratic expression ax^2+bx+c for values a, b, c and x.

    Parameters:
        'a, b, c, x' (integers/floats) - Variables of the quadratic function. 

    Returns: 
        (int/float) - Returns the value of the quadratic function.
    """
    return a*x*x+b*x+c


# Ex B.13 
def GC_content(dna_sequence):
    """
    Function takes as input a DNA molecula. Computes the proportion of the sum of 
    bases G and C over the total lenght of the DNA sequence.

    Parameter:
        'molecule' (str) - DNA sequence

    Returns: 
        (float) - Proportion of the sum of G and C bases over the lenght of the DNA sequence.  
    """
    x = dna_sequence.upper()
    cytosine = x.count("C")
    guanosine = x.count("G")
    length_molecule = len(dna_sequence)
    return (cytosine + guanosine) / length_molecule
