import numpy as np


"""
Timing and Profiling Code:

Examining Runtime:

Why should we time our code?
+ It allows us to pick the optimal coding approach
+ Faster code == more efficient code!

How can we time our code?
+ Calculate runtime with IPython magic command %timeit
+ Magic commands: enhancements on top of normal Python syntax
    + Prefixed by the "%" character
    + See all available magic commands with %lsmagic
    + THEY ARE ONLY AVAILABLE IN IPython!!!
        + I should install a kernal and create a venv...
        
Using %timeit
    Code to be timed:
    import numpy as np
    rand_nums = np.random.rand(1000)

Timed version:
    %timeit rand_nums = np.random.rand(1000)    
    >>> 8.61 ns per loop ....
    
Specifying number of runs/loops:
    Setting the number of runs (-r) and/or loops (-n)
    
    # Set number of runs to 2 (-r2)
    # Set number of loops to 10 (-n10)
    %timeit -r2 -n10 rand_nums = np.random.rand(1000)
    
Using %timeit in cell magic mode (%%timeit) for multiple lines of code:
    %%timeit
    nums = []
    for x in range(10):
        nums.append(x)
        
Saving Output:
    Saving the output to a variable (-o)
    times = %timeit -o rand_nums = np.random.rand(1000)
    print(times.timings)
    print(times.best)
    print(times.worst)
    
Comparing times (creating dict using d1 = dict() or d2 = {}):
    f_time = %timeit -o formal_dict = dict()
    l_time = %timeit -o literal_dict = {}
    diff = (f_time.average - l_time.average) * (10 ** 9)
    print(f'l_time better than f_time by {diff} ns')
"""

"""
Code Profiling for Runtime:
What do we use if we want to time a large code base or see the line-by-line runtimes within a function?

Code Profiling:
 + Detailed stats on frequency and duratin of function calls.
 + Line-by-line analyses
 + Package used: line_profiler (i.e. pip install line_profiler)
"""


def code_profiling_runtime_example():
    heroes = ['Batman', 'Superman', 'Wonder Woman']
    hts = np.array([188.0, 191.0, 183.0])
    wts = np.array([95.0, 101.0, 74.0])
    print(convert_units(heroes, hts, wts))


def convert_units(heroes, heights, weights):
    """Helper for code_profiling_runtime_example()"""
    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]
    hero_data = {}
    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data


"""
Code Profiling For Memory Usage

Quick and dirty approach
"""


def code_profiling_for_memory_usage():
    import sys
    nums_list = [*range(1000)]
    print(sys.getsizeof(nums_list))

    nums_np = np.array(range(1000))
    print(sys.getsizeof(nums_np))


"""
Code profiling: memory
 + Detailed stats on memory consumption
 + Line-by-line analysis
 + Package used: memory_profiler
 + pip install memory_profiler
 + using memory_profiler package:
    %load_ext memory_profiler
    %mprun -f convert_units convert_units(heroes, hts, wts)
 + Functions must be imported when using memory_profiler
    from hero_funcs import convert_units
    %load_ext memory_profiler
    %mprun -f convert_units convert_units(heroes, hts, wts)
 + %mprun output caveats:
    + Inspects memory by querying the operating system
    + Results may differ between platforms and runs
        + Can still observe how each line of code compares to others based on memory consumption.
"""


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


def main():
    combining_objects()
    combining_objects_with_zip()
    counting_with_loops()
    combinations_with_loops()


if __name__ == '__main__':
    main()
