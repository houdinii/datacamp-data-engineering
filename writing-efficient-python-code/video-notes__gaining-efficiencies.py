"""
Gaining Efficiencies

Efficiently combining, counting, and iterating

Pokemon Overview:
 + Trainers (collect Pokemon)
 + Pokemon (fictional animal characters)
 + Pokedex (stores captured Pokemon)

Combining Objects:
Suppose we have two lists, one of Pokemon names, and another of Pokemon Health Points and we want them combined:
"""


def combining_objects():
    names = ['Bulbasaur', 'Charmander', 'Squirtle']
    hps = [45, 39, 44]
    combined = []
    for i, pokemon in enumerate(names):
        combined.append((pokemon, hps[i]))
    print(combined)


def combining_objects_with_zip():
    names = ['Bulbasaur', 'Charmander', 'Squirtle']
    hps = [45, 39, 44]
    combined_zip = zip(names, hps)
    print(type(combined_zip))
    combined_zip_list = [*combined_zip]
    print(combined_zip_list)


"""
The collections module:
 + Part of Python's Standard Library (built-in module)
 + Specialized container datatypes
    + Alternatives to general purpose dict, list, set, and tuple.
 + Notable:
    + namedtuple: tuple subclasses with named fields
    + deque: list-like container with fast appends and pops
    + Counter: dict for counting hashable objects
    + OrderedDict: dict that retains order of entries
    + defaultdict: dict that calls a factory function to supply missing values

Counting with loop:
"""


def counting_with_loops():
    # Each Pokemon's type (720 total)
    poke_types = ['Grass', 'Dark', 'Fire', 'Fire', 'Poison', 'Grass']
    type_counts = {}
    for poke_type in poke_types:
        if poke_type not in type_counts:
            type_counts[poke_type] = 1
        else:
            type_counts[poke_type] += 1
    print(type_counts)

    # A much more efficient approach:
    from collections import Counter
    type_counts = Counter(poke_types)
    print(type_counts)


"""
The itertools module:
 + Part of Python's Standard Library (built-in module)
 + Functional tools for creating and using iterators
 + Notable:
    + Infinite iterators: count, cycle, repeat
    + Finite iterators: accumulate, chain, zip_longest, etc.
    + Combination generators (our focus): product, permutations, combinations
"""


def combinations_with_loops():
    poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']
    combos = []

    for x in poke_types:
        for y in poke_types:
            if x == y:
                continue
            if ((x, y) not in combos) & ((y, x) not in combos):
                combos.append((x, y))
    print(combos)

    # A better way using itertools.combinations()
    from itertools import combinations
    combos_obj = combinations(poke_types, 2)
    print(type(combos_obj))
    print([*combos_obj])


"""
Set Theory:
 + Branch of Mathematics applied to collections of objects.
    + i.e. sets
 + Python has built-in set datatype with accompanying methods:
    + intersection(): All elements that are in both sets.
    + difference(): All elements in one set but not the other.
    + symmetric_difference(): All elements in exactly one set.
    + union(): All elements that are in either set.
 + Fast membership testing:
    + Check if a value exists in a sequence or not.
    + Using the in operator.
"""


def comparing_objects_with_loops():
    list_a = ['Bulbasaur', 'Charmander', 'Squirtle']
    list_b = ['Caterpie', 'Pidgey', 'Squirtle']

    # Show objects in both lists - the inefficient way (433ns):
    in_common = []
    for pokemon_a in list_a:
        for pokemon_b in list_b:
            if pokemon_a == pokemon_b:
                in_common.append(pokemon_a)
    print(in_common)

    # Using sets (141ns):
    set_a = set(list_a)
    print(set_a)
    set_b = set(list_b)
    print(set_b)
    print(set_a.intersection(set_b))

    # Set difference:
    print(set_a.difference(set_b))

    # Symmetric Difference:
    print(set_a.symmetric_difference(set_b))

    #  Unions:
    print(set_a.union(set_b))


def uniques_with_sets():
    primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', "Fire", "Water"]
    unique_types = []
    # Inefficient way:
    for prim_type in primary_types:
        if prim_type not in unique_types:
            unique_types.append(prim_type)
    print(unique_types)

    # OR WE COULD:
    unique_types_set = set(primary_types)
    print(unique_types_set)


def main():
    uniques_with_sets()


if __name__ == '__main__':
    main()
