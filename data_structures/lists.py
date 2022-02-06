from ast import Expression


letters = ['a', 'b', 'c']

matrix = [[0, 1], [2, 3]]

dup = [0] * 5

print(dup)

concat = dup + letters

print(concat)

numbers = list(range(20))

print(numbers)

chars = list('Hello World!')

print(chars)

# Length
print(len(chars))

# Search backwards
print(chars[-1])

# Slice - [:] creates copy like JS
print(chars[6:11])

# step
print(numbers[::2])
print(numbers[::-1])  # reverse the order

# List unpacking
numbers = [1, 2, 3, 3, 3, 3, 3, 3, 3]
first, second, *rest = numbers
print(first, second, rest)  # variables must = length
first, second, *rest = numbers
print(first, second, rest)  # *variable is similar to ...rest
first, *rest, last = numbers
print(first, rest, last)


# Looping with Lists
letters = ['a', 'b', 'c', 'd', 'e']
for letter in enumerate(letters):  # omitting enumerate gives only the value
    print(letter)

# Adding to Lists
letters.append('f')  # adds to the end
letters.insert(0, '0')  # like splice

# Removing from Lists
letters.pop(0)  # ommitting the index will pop the last value
# removes the FIRST occurance. Use Loops to do all occurances
letters.remove('b')
del letters[0:3]  # like pop but with a range of values
letters.clear()  # clears list
print(letters)

# if searching for something
if 'd' in letters:
    # does not exist will throw error (not -1 like JS)
    print(letters.index('z'))

# Sorting Lists
numbers = [7, 5, 8, 2, 9, 3, 4, 4]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# does not mutate like sort() does but makes a copy
print(sorted(numbers, reverse=True))
print(numbers)

# sorting complex items
items = [
    ('items1', 17),
    ('items2', 15),
    ('items3', 19),
]


def sort_items(item):
    return item[1]


items.sort(key=sort_items)
print(items)

items.sort(key=lambda item: item[1])  # same thing using lambda function
print(items)


#Mapping
items = [
    ('items1', 17),
    ('items2', 15),
    ('items3', 19),
]

mapped = map(lambda item: item[1], items)
print(mapped)
for item in mapped:
    print(item)

listMap = list(map(lambda item: item[1], items)) #Note using the variable mapped here does not work and returns an empty array
print(listMap)

#Filtering
filteredList = list(filter(lambda item: item[1] >= 17, items))
print(filteredList)

#listComprehension
[item[1] for item in items] #produces map result
[item for item in items if item[1] >=17] #produces filter result

#zipFunctions used for multiple lists
list1 = [1,2,3]
list2 = [10,20,30]
print((list(zip('123', list1, list2))))