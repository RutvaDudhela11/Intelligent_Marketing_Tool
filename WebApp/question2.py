# Question 2: 
# Write a Python program to combine two dictionary by adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(d1.keys())
# d1.keys
# D =dict()
d = dict({'a': 0, 'b': 0, 'd': 0, 'c': 0})
# for i in d1:
#     # print(i)
#     for j in d2:
#         if i == j:
#             print(i, j)
#             d = d1.get(str(i)) + d2.get(str(j))
        
#     D = {str(i): d ,}
#     print(D)
            # print(d)
    # print(d)
for k in d:
    for i in d1:
        for j in d2:
            if i == k and j == k :
                d[k] = d1[i] + d2[j]
                # if i != j and i == k:
                #     d[k] = d1[i]
            # elif i != j and j == k:
            #     d[k] = d2[j]
            # elif i != j and i ==k:
            #     d[k] = d1[i]
print(d)
            
# A = d1.get('a') + d2.get('a')
# # print(A)
# B = d1.get('b') + d2.get('b')
# print(B)
# combined = {'a': d1.get('a') + d2.get('a'), 'b': d1.get('b') + d2.get('a'), 'c': 300, 'd': 400}
# combined = {'a': A, 'b': B, 'c': 300, 'd': 400}
# print(combined)



# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# Question 3:

# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
string = "google.com"
d3 = dict()
# count=0
# print(d3)
for i in string:
    # count = 0
    # print(i)
    count = string.count(i)
    d3.update({i : count})
    # d = {i:count ,}
    # s = d.items()
    # print(s)
print("Expected Result :", d3)    