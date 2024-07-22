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
