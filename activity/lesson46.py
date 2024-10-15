lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

print("Multiplication on List :", lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)


# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

# remove particular element
my_dict.pop('age')
print(my_dict)

# access a particular element
print("Address :", my_dict.get('address'))

# remove all the elements
my_dict.clear()
print(my_dict)


def test(lst):
	result = {}
	for item in lst:
		result[item[0]] = item[1:]
	return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted  lists to a dictionary:")
print(test(students))

