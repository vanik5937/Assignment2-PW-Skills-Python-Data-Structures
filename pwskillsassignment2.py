# -*- coding: utf-8 -*-
"""PWSkillsAssignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CD3Lwhcl5DQW9FvM8tEPNGhzqzSWzDIS

**1. Discuss string slicing and provide examples.**

It is a way to access a part of a string. It allows us to obtain a substring by specifying a range of indices.
Its syntax is written as follows:
string[start:stop:step]
Start is the starting index of  the slice
Stop is ending index of the slice (exclusive)
Step value determines the stride between each index.
eg.
s= "ajay bijay"
substring = [0:5:2] # substring will be "aa "

**2. Explain the key features of lists in Python.**

Following are its key features:
i. Ordered Collection: Lists maintain the order of elements as they are added. This means that elements can be accessed by their index positions.
ii. Mutable: It is mutable, meaning their contents can be changed after creation. Elements can be added, removed, or modified.
iii.Indexing and Slicing: It supports indexing and slicing to access some parts of the list.
iv. Builtin methods: Following are its builtin methods:
a. append()
b. insert()
c. remove()
d. pop()
e. clear(), etc
v. Nested Lists: It can contain lists inside list.

**3. Describe how to access, modify, and delete elements in a list with examples.**
list = [10,20,"ram",40]
i. Access: print(list[0]) # 10
ii. Modify: list[0] = 90
            list[2] = "Shyam"
            print(list) # [90, 20, 'Shyam', 40]
iii. Delete: del list[3] # [10, 20, 'Shyam']

**4. Compare and contrast tuples and lists with examples.**

Lists are mutable whereas Tuples are immutable
list = [1,2,3,4]
tuple = (1,2,3,4)
Lists are defined using square brackets whereas Tuples are defined using parentheses.
Lists are slightly slower than tuples due to mutability whereas Tuples are faster than list due to their immutability

**5. Describe the key features of sets and provide examples of their use.**

Following are its key features:
i. Unordered Collections: Sets do not maintain any order of elements.
ii. Unique Elements: Each element in a set must is unique.
iii. Mutable: Sets are mutable
iv. No Indexing or Slicing: Sets are unordered. .'., they do not support indexing or slicing.
eg.
set1 = {1,2,3,4}
print(set1) #{1,2,3,4}
set2 = {1,2,2,3,3,4,5}
print(set2) #{1,2,3,4}

**6. Discuss the use cases of tuples and sets in Python programming**

Tuples are best used when:
i. The collection of items should not change.
ii.We need a fixed, ordered sequence of elements.
iii. We need to return multiple values from a function.

Sets are best used when:
i. We need to remove rendundant elements.
ii.We need to perform mathematical set operations.
iii.We need to keep track of a dynamic collection of unique items.

**7.Describe how to add, modify, and delete items in a dictionary with examples.**
dict = {}
i. Add: dict[1] = 2
        dict[2] = 3
        dict[3] = 4
        #{1:2, 2:3, 3:4}
ii. Modify: dict[1] = 5
        #{1:5, 2:3, 3:4}
iii. Delete:  del dict[1]
        #{2:3, 3:4}
    dict.pop(2)
        #{3:4}
    dict.clear()
        #{}

**8. Discuss the importance of dictionary keys being immutable and provide examples.**

i. Hashability: Hashable objects have a hash value that does not change during their lifetime. This hash value is used to quickly compare dictionary keys during lookups.
ii.Efficiency: Immutable objects ensure that the key's hash value remains constant, allowing Python to optimize dictionary operations like inserts, deletes, and lookups.
This optimization leads to efficient time complexity for these operations, typically O(1), meaning the operation takes constant time regardless of the dictionary size.
iii. Consistency: Immutability guarantees that once a key is added to a dictionary, it will always refer to the same value until explicitly removed.
eg:
my_dict = {1: 'one', 2: 'two'}
# This will raise an Error
my_dict = {[1, 2, 3]: 'list'}
"""