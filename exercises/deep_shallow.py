import copy

"""Deep/Shallow Copy Lista"""

# Deep Copy List

original_list = [[1, 2, 3], 4, 5, 6, [7, 8, 9]]
deep_copied_list = copy.deepcopy(original_list)

# Modificăm copia adâncă pentru a arăta că modificările nu afectează originalul
deep_copied_list[0][0] = 99

# Verificăm modificările
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

# Shallow Copy Lista

original_list = [[1, 2, 3], 4, 5, 6, [7, 8, 9]]
shallow_copied_list = copy.copy(original_list)

# Modificăm copia superficială pentru a arăta că modificările afectează originalul
shallow_copied_list[0][0] = 99

# Verificăm modificările
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

"""Deep/Shallow Copy Dictionar"""

# Deep Copy Dictionar

original_dict = {'a': [1, 2, 3], 'b': 4, 'c': 5}
deep_copied_dict = copy.deepcopy(original_dict)

# Modificăm copia adâncă pentru a arăta că modificările nu afectează originalul
deep_copied_dict['a'][0] = 99

# Verificăm modificările
print("Original Dictionary:", original_dict)
print("Deep Copied Dictionary:", deep_copied_dict)

# Shallow Copy Dictionar

import copy

original_dict = {'a': [1, 2, 3], 'b': 4, 'c': 5}

# Shallow Copy pentru Dicționar
shallow_copied_dict = copy.copy(original_dict)

# Modificăm copia superficială pentru a arăta că modificările afectează originalul
shallow_copied_dict['a'][0] = 99

# Verificăm modificările
print("Original Dictionary:", original_dict)
print("Shallow Copied Dictionary:", shallow_copied_dict)
