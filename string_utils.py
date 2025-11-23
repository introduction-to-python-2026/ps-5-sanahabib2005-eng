


def split_before_uppercases(formula):
    if not formula:
        return []
    split_formula = []
    start = 0
    for i in range(1,len(formula)):
        if (formula[i]).isupper():
           split_formula.append(formula[start:i])
           start = i
    split_formula.append(formula[start:])
    return split_formula

def split_at_digit(formula):
     for digit_location in range(len(formula)):
        if formula[digit_location].isdigit():
           return formula[:digit_location] , int(formula[digit_location:])
           break

     return (formula , 1)
    
def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    dictionary = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, count = split_at_digit(atom)
        dictionary[atom_name] = dictionary.get(atom_name,0)+ count
    return dictionary



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
