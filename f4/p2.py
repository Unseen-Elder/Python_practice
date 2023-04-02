#list methods

l1=[33,51,12,67,9,72,61,44,33,11,56,24,40]
l2=[12,33,14,61,97]
l3=[22,43,91,62,54,9]
l4=[3,4,22,49,52,6]

print(l1)
print(l1.sort()) # cant print directly , first i have to sort then print
print(l1)

print(l2)
l2.reverse()
print(l2)

print(l3)
l3.append(21) #adds 21 as new element at the end of list
print(l3)

print(l4)
l4.insert(3,11) #add 11 as new element at index 3
print(l4)