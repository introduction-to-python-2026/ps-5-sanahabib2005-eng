


def split_before_uppercases(formula):
    if not formula:
        return []
    split_formula = []
    start = 0
    for i in range(1, len(formula)):
        # Check for new capital letter, assuming it's the start of a new element
        if (formula[i]).isupper():
            split_formula.append(formula[start:i])
            start = i
            
    # Add the last segment
    split_formula.append(formula[start:])
    return split_formula

def split_at_digit(formula):
    # Iterate to find the first digit
    for digit_location in range(len(formula)):
        if formula[digit_location].isdigit():
            # Atom name is everything before the digit, count is the rest as an int
            return formula[:digit_location], int(formula[digit_location:])

    # If no digit is found, the count is 1 (e.g., 'O' or 'Fe')
    return (formula, 1)
    
def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    atom_counts = {} # Use a more descriptive variable name
    
    # 1. Split the formula into element/count chunks (e.g., 'H2O' -> ['H2', 'O'])
    for atom_chunk in split_before_uppercases(molecular_formula):
        
        # 2. Split each chunk into the name and the count (e.g., 'H2' -> 'H', 2)
        atom_name, count = split_at_digit(atom_chunk)
        
        # 3. FIX: Add or update the count in the dictionary
        atom_counts[atom_name] = count
        
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
