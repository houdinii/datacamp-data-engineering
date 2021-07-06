list1 = ["a", "b", "c", "d", "e", "f"]

# Comprehension which simply duplicates list1
print([i for i in list1])

# Comprehension using simple if statement
print([i for i in list1 if i != "a"])

# Transform elements of a list:
print([i.upper() for i in list1])

# If...Else statement
print([i.upper() if i != "a" else i for i in list1])

# ADVANCED LIST COMPREHENSION

# Use elements of 2 lists
l1 = ["a", "b"]
l2 = [1, 2]
print([i + str(j) for i in l1 for j in l2])

# Example: Get the email addresses from a list of domains
l1 = ["billy@gmail.com", "george@hotmail.com", "www.billy.com", "python.com", "mike@predictivehacks.com"]
domains = ['gmail.com', "hotmail.com"]

# It searches for email addresses with domains that are in the list "domains"
in_list = [i for i in l1 for j in domains if j in str(i)]
print(in_list)

# Create list of tuples
l1 = ["billy", "mike", "george", "italy", "greece"]
print([(i, len(i)) for i in l1])

# Interact with other elements of the list
l1 = [1, 2, 3, 6, 0, 1, 4, 5, 9, 0, 1, 4, 5, 0]
print([l1[i - 1] for i, j in enumerate(l1) if j == 0])

# Dictionary Comprehension
# As with List Comprehension, you can apply the same rules to dictionaries but you have to use curly brackets and set the key and
# value pairs. We will show you some examples.

# Create a dictionary from a list
l1 = ["a", "b", "c", "d", "e", "f"]
print({i: i for i in l1})

# Create dictionary enumerating every item of the list
d1 = {i: j for i, j in enumerate(l1)}
print(d1)

# Iterate over keys & values of a dictionary
# Create dict adding 1 to the keys of d1
print({key + 1: value for key, value in d1.items()})
