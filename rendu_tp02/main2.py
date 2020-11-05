

# --------------------------------------------------------------------------
#                          5. Structures de données
# ---------------------------------------------------------------------------

from collections import deque
from math import pi


print ("5. Structures de données")



fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting a position 4

fruits.reverse()
print (fruits)

fruits.append('grape')
print (fruits)

fruits.sort()
print (fruits)

fruits.pop()
print (fruits)


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print (stack)

stack.pop()
print (stack)

stack.pop()

stack.pop()

print (stack)

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print (queue)                           # Remaining queue in order of arrival


squares = []
for x in range(10):
    squares.append(x**2)

print (squares)


squares = list(map(lambda x: x**2, range(10)))
print (squares)

print ([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])



combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print (combs)


print ([str(round(pi, i)) for i in range(1, 6)])


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print (matrix)


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print (transposed)


transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print (transposed)

print (list(zip(*matrix)))

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print (a)

del a[2:4]
print (a)

del a[:]
print (a)



t = 12345, 54321, 'hello!'
print (t[0])

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)



# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)

print(singleton)
print(len(singleton))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print (a)                                # unique letters in a

print (a - b)                              # letters in a but not in b

print (a | b  )                            # letters in either a or b

print (a & b   )                           # letters in both a and b

print (a ^ b )                             # letters in a or b but not both



