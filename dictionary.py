details = {
    'name': 'Luke',
    'age': 27,
    'Location': 'Kenya'
}
print(details)
print(details['name'])
print(details.get('age'))

# update the dictionary
details['Location'] = 'Uganda'
print(details)

# add a new key-value pair
details['race'] = 'African'
print(details)
