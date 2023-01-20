"""
Student name: Julian Navarro

Function that creates a new file without tabs that were replaced from another
file with a 'tab_length' amount of spaces.

Reminder: Do not refer to other programs when documenting a module like this!
Documentation should usually not assume specific clients for
good generalization/maintainability.
"""

# In MP3, os must only be used to check for whether a file exists
# (which we give to you)
import os


def tabs_to_spaces(filename, tab_length):
    """
    Given a 'filename' and 'tab_lenght', it creates a new file without
    tabs that were replaced with a 'tab_length' amount of spaces. It also
    prints the amount of lines in 'filename' and the tabs that were replaced.

    Arguments:
        - 'filename' (string) - name of the file to analize
        - 'tab_lenght' (int) - number of tab spaces

    Return:
        - 'None'
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
    else:
        file = open(filename,  'r')
        spaced = "spaced" + "_" + filename
        spaced_file = open(spaced, 'w')
        tab_count = 0
        linetab_count = 0
        lst = []
        for line in file:
            if '\t' in line:
                linetab_count += 1
                tab_count += line.count('\t')
                line = line.replace('\t', tab_length * ' ')
            lst.append(line)
        spaced_file.writelines(lst)
        print(f'Lines with tabs: {linetab_count}\nTabs replaced: {tab_count}')
        file.close()
