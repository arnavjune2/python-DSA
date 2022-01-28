"""

hashmap isuse to store key and value pairs
dict[key]---> returns value
dict[new_key]=new_value
key in dict---->boolean(i.e if key is present in dict then True else False)

"""
dict = {1001:["arnav", 89], 1002:["ram", 79], 1002:["shamm", 89]}
print(dict)

#adding into hashmap
dict[1003] = ["raju", 56]

#if you want to print( dict[990]), then it will produce an KeyError so instead we can use dict.get(990)
print(dict.get(990))

#iterating through the hashmap
for key, value in dict.items():
    print(key," ",value)