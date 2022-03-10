#!/usr/bin/python3

# LIST

chars = ["A", "B", "C", "D"]

for char in chars: print(char) 
# OUTPOUT
# A
# B
# C
# D
#-------------------------------------

for index,char in enumerate(chars):
    print(index, char)
# OUTPOUT
# 0 A
# 1 B
# 2 C
# 3 D
#--------------------------------------

for index,char in enumerate(chars, start=2): 
    print(index, char)
#OUTPOUT
# 2 A
# 3 B
# 4 C
# 5 D
#--------------------------------------

joints = ", ".join(chars)
print(chars)
print(joints) 
#OUTPOUT
# ['A', 'B', 'C', 'D']
# A, B, C, D
#--------------------------------------

csv =  "A;B;C;D"
list_csv = csv.split(";")
print(list_csv)
#OUTPUT
# ['A', 'B', 'C', 'D']
#--------------------------------------

# Tuples; Immutable lists, Faster than a list, Secure data


tuple = ("A","B","C","D")

print("A" in tuple) 
#OUTPUT
# TRUE
#---------------------------------------

# SET; List without order and doubles.
# set = {};  set = set()

set = {"A","B","C","D","A"}
print(set)
#OUTPUT 
# The output will always be different because list has no orders ex :
# {'B', 'D', 'C', 'A'}
# {'C', 'A', 'B', 'D'}
#---------------------------------------
set2 = {"A","B"} 
print(set.intersection(set2))
#OUTPUT
# {'A', 'B'}
#---------------------------------------
print(set.difference(set2))
#OUTPUT
# {'D', 'C'}
#---------------------------------------
set3 = {"A","B","Z"}
print(set.union(set3))
#OUTPUT
# {'Z', 'C', 'D', 'A', 'B'}
#---------------------------------------
set.remove("A")
print(set)
#OUTPUT
# {'C', 'D', 'B'}
#---------------------------------------


# DICTONNARIES
 
dictionnary = {"key1":"value1", "keyList":["value1","value2","value3"]}
print(dictionnary["key1"])
#OUTPUT
# Value1
#---------------------------------------
print(dictionnary.get("key3"))
#OUTPUT
# None       (the key doesnt exist so the return in None)
#---------------------------------------
dictionnary.update({"key1":"newValue", "key2":"value4"})
print(dictionnary)
#OUTPUT
# {'key1': 'newValue', 'keyList': ['value1', 'value2', 'value3'], 'key2': 'value4'}
#---------------------------------------
del dictionnary["key1"]
print(dictionnary)
#OUTPUT
# {'keyList': ['value1', 'value2', 'value3'], 'key2': 'value4'}.
#---------------------------------------
var = dictionnary.pop("key2")
print(dictionnary)
print(var)
#OUTPUT
# {'keyList': ['value1', 'value2', 'value3']}
# value4
#---------------------------------------
dictionnary2 = {"key1":"value1", "keyList":["value1","value2","value3"]}
print(dictionnary2.keys()) 
#OUTPUT
# dict_keys(['key1', 'keyList'])
print(dictionnary2.values()) 
#OUTPUT
# dict_values(['value1', ['value1', 'value2', 'value3']])
print(dictionnary2.items()) 
#OUTPUT
# dict_items([('key1', 'value1'), ('keyList', ['value1', 'value2', 'value3'])])
for key, value in dictionnary2.items():
    print(key, value)
#OUTPUT
# key1 value1
# keyList ['value1', 'value2', 'value3']
