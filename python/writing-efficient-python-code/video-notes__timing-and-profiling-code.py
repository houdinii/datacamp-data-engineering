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


def main():
    pass


if __name__ == '__main__':
    main()
