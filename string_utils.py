


def split_by_capitals(formula): # Renamed from split_before_uppercases
    if not formula:
        return []
    split_formula = []
    start = 0
    for i in range(1, len(formula)):
        if (formula[i]).isupper():
            split_formula.append(formula[start:i])
            start = i
            
    split_formula.append(formula[start:])
    return split_formula

def split_at_number(formula): # Renamed from split_at_digit
    for digit_location in range(len(formula)):
        if formula[digit_location].isdigit():
            return formula[:digit_location], int(formula[digit_location:])
    
    return (formula, 1)
    
def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.      Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        atom_counts[atom_name] = atom_count

    # Step 3: Return the completed dictionary
    return atom_counts



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
