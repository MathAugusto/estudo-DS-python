# List Comprehensions
lsta = [1, 2, 3, 4]

print([item**2 for item in lsta])

#-------------------------------------------------------
# Functions
def quadrado(param):
    return param**2
y = quadrado(6)

print(y)

#-------------------------------------------------------
# Lambda
lambda var: var**2

#-------------------------------------------------------
# Map
seq1 = [1, 2, 3, 4, 5]
seq2 = [5, 4, 3, 2, 1]

map(quadrado, seq1)

print(list(map(quadrado, seq1)))

# Map com Lambda
print(list(map(lambda x: x**2, seq2)))

#-------------------------------------------------------
# Filter (com Lambda)
print(list(filter(lambda item: item%2 == 0, seq2)))
print(list(filter(lambda item: item%2 != 0, seq2)))
