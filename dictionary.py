details = {
    'name': 'Luke',
    'age': 27,
    'Location': 'Kenya'
}
print(details)
print(details['name'])
print(details.get('age'))

# update the dictionary
details['Location'] = 'Britain'
print(details)

# add a new key-value pair
details['race'] = 'African'
details['hometown'] = 'Kitale'
details['tribe'] = 'Luhya'
print(details)

# remove a particular key-value pair
details.pop('race')
print(details)

# remove the last key-value pair
details.popitem()
print(details)

# delete a key-value pair
del details['hometown']
print(details)

# create a dictionary using the comprehension method
new_details = {x: x**2 for x in range(10)}
print(new_details)

# iterate through the dictionary
details2 = {1: 'Luke', 2: 'John', 3: 'Mary'}
for i in details2:
    print(details2[i])

print(len(details2))
