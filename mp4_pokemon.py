"""
CS1 22fa
Student name: Julian Navarro
Date: November 5 2022

Original author: El Hovik
Credit to Zane Reeves for helping on updates for 22fa!

Provides a collection of utility functions to help a player manage
data about a Pokedex (pokedex.csv) and their running Pokemon collection
(collected.csv). Note that pokedex.csv is a reference dataset that should
not be changed, while functionality to add, remove, and rename rows in
collected.csv is provided in the functions below.

Note:
- In this program, you will see references to "pokedex id" (pid) and
  "collected id" (cid). A Pokedex id is simply the unique identifier
  for a Pokemon species in the Pokedex (e.g. pid of 1 for Bulbasaur,
  25 for Pikachu, etc.). A cid refers to the "collected id" in a player's
  collection of Pokemon, and is _not_ stored in pokedex.csv OR collected.csv.
  The cid is different than pid so that a player can choose one of their
  collected Pokemon from collected.csv to rename, abandon, or play a battle
  with. Because a player may have more than one of the same type of Pokemon,
  this cid is important to distinguish two Pokemon of the same species, and
  is determined by the row # in collected.csv (e.g. the first Pokemon in
  collected.csv will always have a cid of 1, but may have a different pid
  depending on the Pokemon species).

***************************************************************
For full credit, you must remove all TODOs and pass statements.
***************************************************************
"""
import csv
import os  # only used for checking if a file exists
# A helper library that provides an interface to load move data and access
# methods for formatting and checking attributes of a Pokemon's move.
from Move import Move

# Provided starter code for program constants.
# Columns in collected.csv, which may be useful in some functions (e.g.
# fieldnames)
COLLECTED_COLUMNS = ['pid', 'name', 'nickname', 'level',
                     'type', 'weakness', 'hp']

STARTER_LVL, MAX_LVL = 5, 100


# Note: Exercise 1 Utility Functions were introduced in Lecture 12; students
# who followed along may use the code shown in lecture, but the rest of the
# functions must solely be their own work.
# Exercise 1.a.
def load_data(filename):
    """
    Returns a list of dictionary rows given a CSV `filename`.
    If the file doesn't exist, prints a message and returns [].

    Arguments:
        - `filename` (str) - filename to load (should be .csv file)

    Returns:
        - list[dict] - List of row dicts mapping each column in the file to the
                       respective row's value at that column
                       ([] if file wasn't found or was empty)
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
        return []
    else:
        lst = []
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                lst.append(row)
        return lst


# Exercise 1.b.
def clear_data(filename):
    """
    Clears the data for the given CSV file, leaving only the
    header column. Prints an error message if the file isn't
    found, otherwise prints a success message.

    Arguments:
        - `filename` (str) filename corresponding to a non-empty CSV file.

    Returns:
        - `None`
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
    else:
        with open(filename) as file:
            header = file.readline()
        with open(filename, 'w') as file_clear:
            file_clear.write(header)
        print(f'{filename} data successfully cleared!')


# Exercise 2.a.
def load_pokedex():
    """
    Loads Pokedex data from pokedex.csv and returns the result
    list of dictionary rows.

    Arguemnts:
        - N/A

    Returns:
        - list[dict]
    """
    return load_data("pokedex.csv")


# Exercise 2.b.
def load_collected():
    """
    Loads collected data from collected.csv and returns the result
    list of dictionary rows.

    Arguments:
        - N/A

    Returns:
        - list[dict]
    """
    return load_data("collected.csv")


# Exercise 3.a.
def display_pokedex(pokedex):
    """
    Prints a listing of all Pokemon in the passed `pokedex` (a list of
    dict rows from pokedex.csv) representing Pokedex data, in the following
    format per row:
    #<pid>: <name> (<pokemon type>)

    Example:
    #1: Bulbasaur (Grass)
    #2: Venusaur (Grass)
    ...
    #151: Mew (Psychic)

    Argument:
        - `pokedex` (list[dict]) - list of pokemon row dicts from pokedex.csv

    Returns:
        - `None`
    """
    print('-' * 30)
    print('Full Pokedex Information:')
    print('-' * 30)
    for row in pokedex:
        poke_number = row['pid']
        name = row['name']
        poke_type = row['type']
        display = f'#{poke_number}: {name} ({poke_type})'
        print(display)


# Exercise 3.b.
def display_collected(collected):
    """
    Prints a listing of all _collected_ Pokemon in the list of
    collected dicts representing data specific to a player's current collection
    (see collected.csv) which is different than a Pokedex row. Each
    line is printed in the following format, where <cid> is the row #,
    starting with 1 (different than 'pid', which is the unique Pokedex id):
    <cid>: <name> "<nickname>" (<pokemon type>)

    Example, in the case collected.csv has only four rows:
    1: Pikachu "Sparky" (Electric)
    2: Magikarp "Finny" (Water)
    3: Mew "Mu" (Psychic)
    4: Paras "PARAS" (Bug)

    Argument:
        - `collected` (list[dict] - list of row dicts from collected.csv

    Returns:
        - `None`
    """
    if not collected:
        print('No Pokemon collected yet.')
    else:
        print('-' * 30)
        print('Your collected Pokemon:')
        print('-' * 30)
        cid = 1
        for row in collected:
            name = row['name']
            nickname = row["nickname"]
            poke_type = row['type']
            display = f'{cid}: {name} "{nickname}" ({poke_type})'
            cid += 1
            print(display)


# Exercise 4
def add_pokemon(pokemon):
    """
    Given a dict corresponding to a row in pokedex.csv or collected.csv,
    creates a new entry to collected.csv using `COLLECTED_COLUMNS` to
    populate a new row that is appended to collected.csv (a dict row from
    pokedex.csv has only some columns that are shared in collected.csv).
    You can assume that the given `pokemon` has keys for pid, name, type,
    weakness, hp, but it may or may not have a level key. Any other keys
    in the `pokemon` will be ignored for this function.

    Adds the given pokemon to the collected.csv dataset, first prompting
    the user if they want to give the new collected Pokemon a nickname.
    If the user chooses not to give a nickname, the collected Pokemon's
    nickname defaults to its name in uppercase
    (e.g. 'Bulbasaur' -> 'BULBASAUR'). If the given dict does not have a
    'level' key, the row added to collected.csv will have a default level of
    `STARTER_LVL`.

    The row will be appended in the following format to match the
    COLLECTED_COLUMNS:
    pid,name,nickname,level,type,weakness,hp

    Examples:
    25,Pikachu,Sparky,7,Electric,Ground,160
    25,Pikachu,PIKACHU,5,Electric,Ground,160
    1,Bulbasaur,Bulby,5,Grass,Fire,200

    Arguments:
        - `pokemon` (dict) - dict to process to _filter_ information to append
          to a new collected Pokemon to collected.csv.

    Returns:
        - `None`
    """
    name = pokemon['name']
    nickname = ''
    prompt = input(
        f'Do you want to give a name to your new {name} (y for yes)? ')
    if prompt.lower() == 'y':
        while not nickname:
            nickname = input('What nickname do you want to give? ')
    else:
        # Default the nickname to the UPPERCASE name
        nickname = name.upper()
    pokemon['nickname'] = nickname

    level = STARTER_LVL
    if 'level' in pokemon:
        level = pokemon['level']
    pokemon['level'] = level
    rows = {}
    with open('collected.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=COLLECTED_COLUMNS)
        for heading in COLLECTED_COLUMNS:
            value = pokemon[heading]
            rows[heading] = value
        writer.writerow(rows)


# Exercise 5
def abandon_pokemon():
    """
    Prompts the user to choose a Pokemon they want to say goodbye to
    (removing it from their collected.csv Pokemon). A user is expected to
    provide a valid "collected id", where 1 is the first Pokemon and N
    the Nth Pokemon in their collected dataset. If an invalid cid is
    provided, prints an "Invalid cid #." message. Otherwise, removes
    the corresponding Pokemon from their collection.

    Returns:
        - `None`
    """
    collected = load_collected()
    display_collected(collected)
    cid = input('Which Pokemon do you want to say goodbye to (Enter #)? ')
    cid = int(cid)
    if cid < 1 or cid > len(collected):
        print("Invalid cid #.")
    else:
        poke_name = collected[cid-1]['name']
        del collected[cid-1]
        with open('collected.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=COLLECTED_COLUMNS)
            writer.writeheader()
            for row in collected:
                writer.writerow(row)
        print(f'Successfully said goodbye {poke_name}!')


# Exercise 6
def rename_pokemon(cid, new_name, collected):
    """
    Renames a Pokemon using the given "collected ID" to the given
    `new_name` string, where the first element in `collected` is considered
    to have a `cid` of 1, and the last `cid` is equal to the # of elements
    in `collected`.

    If `cid` is < 1 or > # of elements in `collected`, prints an error message.
    Otherwise, updates collected.csv appropriately and prints a
    success message.

    Arguments:
        - `cid` (int) - position of Pokemon to update in `collected`
        - `new_name` (str) - new name to give the collected Pokemon
        - `collected` (list[dict]) - list of dictionaries from collected.csv

    Returns:
        - `None`
    """
    collected = load_collected()
    display_collected(collected)
    cid = int(cid)
    if cid < 1 or cid > len(collected):
        print("Invalid cid #.")
    else:
        poke_name = collected[cid-1]['name']
        collected[cid-1]['nickname'] = new_name
        with open('collected.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=COLLECTED_COLUMNS)
            writer.writeheader()
            for row in collected:
                writer.writerow(row)
        print(f'Successfully renamed {poke_name} to {new_name}!')


# Exercise 7
def load_moves():
    """
    Returns a constructed dictionary mapping move names to Move objects
    using data from moves.csv. Assuming no duplicate move names in moves.csv,
    the returned dictionary will have as many keys as rows in moves.csv.

    Returns:
        - dict[str -> Move] - dictionary mapping move names to Move objects.
    """
    moves_dict = {}
    with open('moves.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            name = row['name']
            move_type = row['type']
            accuracy = row['accuracy']
            dp = row['dp']
            buff = row['buff']
            buff_amt = row['buff_amt']
            move = Move(name, move_type, accuracy, dp, buff, buff_amt)
            moves_dict[name] = move
    return moves_dict


# Exercise 8
def generate_move_list(pokemon):
    """
    Given a `pokemon` dictionary (with keys for each column in pokedex.csv)
    returns a list of all non-empty move values. The returned list will
    have between 1 and 4 elements, depending on how many non-empty move
    _values_ are in `pokemon`.

    Arguments:
        - `pokemon` (dict) - row dictionary from pokedex.csv

    Returns:
        - list[str] - list of move name strings
    """
    moves = []
    for i in range(4):
        move = "move" + str(i+1)
        if pokemon[move] != '':
            moves.append(pokemon[move])
    return moves
