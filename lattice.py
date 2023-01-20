"""
CS 1 22fa
MP6: Crystal Lattices
Student Name: Julian Navarro

A program that defines a simple cubic lattice class representing an cubical
structures of atoms.
"""
import math
from atom import Atom


class CubicLattice():
    """
    Simple class representing a cubic lattice.

    Atributes:
        - lparam (int): side lenght of the cubic lattice
        - atoms (list): list of atoms

    """
    def __init__(self, lparam, atoms=[], in_filename=None):
        """
        Constructs an lattice instance representing the atoms with
        side lenght 'lparam'.

        Arguments:
            - lparam (int): side lenght of the cubic lattice
            - atoms (list): list of atoms

        Raises:
            - ValueError if 'lparam' is not positive.
        """
        if in_filename is None:
            self.atoms = atoms
        else:
            self.atoms = self.get_atoms_from_xyz(in_filename)
        if lparam <= 0:
            raise ValueError('lparam must be positive.')
        self.lparam = lparam

    def get_lattice_parameter(self):
        """
        Functions does not take anything and returns side
        lenght of a cubic lattice.
        Arguments:
            -None

        Returns:
            -(int): side lenght of the cubic lattice
        """
        return self.lparam

    def get_cell_volume(self):
        """
        Function takes no argument and returns the volume of
        the cubic lattice in Angstrom units.

        Arguments:
            - None

        Returns:
            - (int/float): Volume of the cubic lattice in Angstrom units.
        """
        return (self.lparam)**3

    def get_unique_elements(self):
        """
        Function takes no arguments and returns the unique elements
        without repetition of the Cubic lattice
        Arguments:
            -None

        Returns:
            - lst: Returns list of unique element names
        """
        elements_lst = []
        for atom in self.atoms:
            if atom.element not in elements_lst:
                elements_lst.append(str(atom.element))
        return elements_lst

    def get_number_atoms(self):
        """
        Function takes no argument and returns the number of collected
        atoms inside a unit cell.
        Arguemnts:
            - None

        Returns:
            - (float): Number of atoms collected in a given crystal lattice.
        """
        number_atoms = 0
        for atom in self.atoms:
            if is_corner(atom.coordinates, self.lparam):
                number_atoms += 1 / 8
            elif is_cell_center(atom.coordinates, self.lparam):
                number_atoms += 1.0
            elif is_face_center(atom.coordinates, self.lparam):
                number_atoms += 1 / 2
        return number_atoms

    def get_inverted_cell(self):
        """
        Function takes no arguments and retuns the inverse of
        every single atom in the cubic lattice.

        Arguemnts:
            -none

        Returns:
            - CubicLattice: Returns the inverse of every element.
        """
        atom = []
        for lea in self.atoms:
            coord = lea.coordinates
            x, y, z = coord
            new_coord = (abs(x - self.lparam), abs(y - self.lparam),
                         abs(z - self.lparam))
            atom.append(Atom(lea.element, new_coord))
        lattice = CubicLattice(self.lparam, atom)
        return lattice

    def as_xyz(self, crystal_name):
        """
        Returns a string representation of the crystal given
        a specified `crystal_name` that is in standard .xyz file format.

        An XYZ file format is strictly as follows (guaranteeing each
        Atom_I_Element line to be comprised of 4 components):

        # of atoms N
        Name of the crystal (basically a comment)
        Atom_1_Element Atom_1_X Atom_1_Y Atom_1_Z
        Atom_2_Element Atom_2_X Atom_2_X Atom_2_Z
        ...
        Atom_N_Element Atom_N_X Atom_N_Y Atom_N_Z

        For example (16 lines total):
        14
        Aluminum FCC
        Al 0 0 0
        ...
        Al 2.0 2.0 4

        Arguments:
            - crystal_name (str): Name of crystal to specify (the second
              line in .xyz format)

        Returns:
            - (str) .xyz data format of crystal, with each line ending with
              '\n' (including the last)
        """
        lst_atoms = []
        for atom in self.atoms:
            lst_atoms.append(str(atom))
        number_atoms = len(lst_atoms)
        atoms = "\n".join(lst_atoms)
        return f'{number_atoms}\n{crystal_name}\n{atoms}\n'

    def write_to_xyz(self, crystal_name, out_filename):
        """
        Writes the current crystal to an XYZ file, which is a standard
        file format compatible with 3D crystal-viewing software.
        See `CubicLattice.as_xyz` for more information on the XYZ
        representation.

        Note: Overwrites file if one already exists.

        Arguments:
            - crystal_name (str): Crystal name; the second line in .xyz file.
            - out_filename (str): Filename to write to (should end in .xyz)

        Returns:
            - None (crystal data is written to `out_filename`)
        """
        with open(out_filename, 'w') as file:
            file_body = self.as_xyz(crystal_name)
            file.writelines(file_body)

    def get_atoms_from_xyz(self, in_filename):
        """
        Given an in_filename, returns a list of Atoms created from the file
        specifications, which should be in valid .xyz format.
        See `CubicLattice.as_xyz` for a summary of a valid XYZ format.

        Note that the (x, y, z) coordinates specified by each XYZ Atom line
        are converted to floats for the list of constructed Atoms.

        Arguments:
            - in_filename (str): Name of .xyz file to import (e.g. 'ex1.xyz')

        Returns:
            - (list[Atom]): list of Atoms constructed from imported file data

        Raises:
            - FileNotFoundError if `in_filename` doesn't exist
        """
        lst_atoms = []
        with open(in_filename, 'r') as file:
            line = file.readline()
            line = file.readline()
            line = file.readline()
            while line != '':
                atom = line.split()
                element = atom[0]
                coords = (atom[1], atom[2], atom[3])
                lst_atoms.append(Atom(element, coords))
                line = file.readline()
        return lst_atoms


# ----------------------------------------
# END CubicLattice class definition
# ----------------------------------------
# 3 helper _functions_ for lattice coordinates; note that these
# generalize for any 3D cube representation, not just 3D crystal lattices.
# DO NOT CHANGE these three functions.
def is_corner(coordinates, length):
    """
    Returns whether the given coordinates are on a corner of a cube with
    side length `length`.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff passed coordinates match corners of `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    for coord in coordinates:
        # By definition, each x, y, z value in a coordinate must be 0 or
        # the length of the cube
        if coord != 0 and coord != length:
            return False
    return True


def is_cell_center(coordinates, length):
    """
    Returns whether the given coordinates are at the center of a
    cube with side length `length`.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff coordinates are the center of `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    for coord in coordinates:
        # By definition, each x, y, z value in a coordinate must be length/2
        # if it is the cube's center
        if coord != length / 2:
            return False
    return True


def is_face_center(coordinates, length):
    """
    Returns whether the given coordinates are on the center of a cube's _face_
    with side length `length`. In other words, they are not at one of the 8
    corners or the center of the cube.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff coordinates are at the center of any of the 6
                  faces of a `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    # By definition, coordinates must not be a corner or the center of the cube
    return not (is_corner(coordinates, length) or
                is_cell_center(coordinates, length))
