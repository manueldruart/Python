#!/usr/bin/python3

#------------------CONDITIONS---------------#

var = "youtube"
if var == "manu":
    print("True")
elif var == "youtube":
    print("YOUTUBE")     
else:
    print("False")
#OUTPUT
# YOUTUBE
#---------------------------

var2 = "manu"
active = False
if var == "manu" and active:
    print("True")
elif var == "youtube":
    print("YOUTUBE")     
else:
    print("False")
#OUTPUT
# False
#---------------------------

list = ["A","B","C"]
list2 = ["A","B","C"]

if list == list2:
    print("same value")
else:
    print("Different values")
#OUTPUT
# same value
if list is list2:
    print("same value")
else:
    print("Different values")
#OUTPUT
# Different values    (Objects are different so return different values even if the objects values are similar)
list3 = list
if list is list3:
    print("same value")
else:
    print("Different values")
#OUTPUT
# same value (Objects are similar so return "same value")
 
obj = False
if obj:
    print("It's True")
else:
    print("It's False")
#OUTPUT
# It's False


#------------------ LOOP : For, While, Break, Continue ---------------#

# +++++++++ FOR ++++++++++

chars = ["A", "B", "C", "D"]

for char in chars:
    if char == "C":
        break
    print(char)
#OUTPUT
# A
# B
#------------------
for char in chars:
    if char == "C":
        continue
    print(char)
#OUTPUT
# A
# B
# D
#------------------
nums = ["1","2","3","4"]
for char in chars:
    for num in nums:
        print(char, num)
#OUTPUT
# #OUTPUT
# A 1
# A 2
# A 3
# A 4
# B 1
# B 2
# ......
for char in chars:
    for num in range(6):
        print(char, num)
#OUTPUT 
# A 0
# A 1
# A 2
# A 3
# A 4
# A 5
# B 0
# B 1
# B 2
# B 3
# B 4
# B 5
# C 0
# .......
for char in chars:
    for num in range(100,103):
        print(char, num)
# OUTPUT 
# A 100
# A 101
# A 102
# B 100
# B 101
# B 102
# C 100
# ........

# +++++++++ WHILE ++++++++++

x = 0
while x < 10:
    if x == 5:
        x += 1
        continue
    print("manu")
    x += 1
