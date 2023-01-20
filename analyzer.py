"""
Student name: Julian Navarro Rodriguez

This program analyzes Python programs and prints fucntion information and
file statistics like words, lines and characters.

Reminder: Do not refer to other programs when documenting a module like this!
Documentation should usually not assume specific clients for
good generalization/maintainability.
"""

# In MP3, os must only be used to check for whether a file exists
# (which we give to you).
import os


# Exercise 1.1.
def print_fns(filename):
    """""
    Given a filename, outputs a report of any defined functions in the
    corresponding file, where a function must be defined as a valid Python
    function statement line starting with "def ".

    For example, a program containing a single function "def foo(x, y):"
    would correspond to

    foo(x, y)

    in one line of the output. Prints an error if the filename isn't found.

    Arguments:
        - `filename` (str) - name of file to analyze.

    Returns:
        - `None`
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
    else:
        print(f'Functions in {filename}: ')
        file = open(filename, 'r')
        for line in file:
            if line.startswith("def "):
                line = line.strip()
                no_def = line.replace("def ", "    ")
                func = no_def.replace(":", "")
                print(func)
        file.close()


# Exercise 1.2.
def file_info(filename):
    """
    Given a filename, analyzes the contents of the file, returning a
    dictionary with the following keys:
    - 'words' (word count of file)
    - 'lines' (line count of file)
    - 'characters' (character count of file, including '\n' characters)

    Supports any file extension, and prints an error message if the file
    isn't found.

    Arguments:
        - `filename` (str) - Name of file to analyze

    Returns:
        - (dict) - dictionary of three str keys having int count values
                   (or `None` if filename is invalid)

    """
    file_count = {}

    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')

    else:
        file = open(filename, 'r')
        n = 0
        word_count = 0
        char_count = 0
        for line in file:
            n += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)
        file_count['lines'] = n
        file_count['words'] = word_count
        file_count['characters'] = char_count
        file.close()
        return file_count
