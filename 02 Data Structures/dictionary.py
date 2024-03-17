# dictionary

# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

dictionaryExample = {
    "name": "John",
    "age": 30
}

print(dictionaryExample) #prints {'name': 'John', 'age': 30}

# we can also use the dict function to create a dictionary

dictionaryExample2 = dict(name="John", age=30)

print(dictionaryExample2) #prints {'name': 'John', 'age': 30}

# we can access the items of the dictionary using the keys

print(dictionaryExample["name"]) #prints John

# we can also use the get method to access the items of the dictionary

print(dictionaryExample.get("name")) #prints John

# we can also use the keys method to access the keys of the dictionary

print(dictionaryExample.keys()) #prints dict_keys(['name', 'age'])

# we can also use the values method to access the values of the dictionary

print(dictionaryExample.values()) #prints dict_values(['John', 30])

# we can also use the items method to access the items of the dictionary

print(dictionaryExample.items()) #prints dict_items([('name', 'John'), ('age', 30)])

# we can also use the update method to update the dictionary

dictionaryExample.update({"name": "Jane", "age": 40})

print(dictionaryExample) #prints {'name': 'Jane', 'age': 40}

# we can also use the pop method to remove the item from the dictionary

dictionaryExample.pop("name")

print(dictionaryExample) #prints {'age': 40}

# we can also use the popitem method to remove the last item from the dictionary

dictionaryExample.popitem()

print(dictionaryExample) #prints {}

# we can also use the clear method to remove all the items from the dictionary

dictionaryExample.clear()

print(dictionaryExample) #prints {}

# we can also use the del keyword to delete the dictionary

del dictionaryExample

# we can also use the fromkeys method to create a dictionary with the specified keys and values

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict) #prints {'key1': 0, 'key2': 0, 'key3': 0}

# we can also use the setdefault method to return the value of the specified key, if the key does not exist, insert the key, with the specified value

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

x = car.setdefault("model", "Bronco")

print(x) #prints Mustang

# we can also use the copy method to copy the dictionary

car2 = car.copy()

print(car2) #prints {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
