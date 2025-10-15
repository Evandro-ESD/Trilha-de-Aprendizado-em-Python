string = "evandro dos santos"
print(string.capitalize())

# & → interseção

# | → união

# - → diferença

# ^ → diferença simétrica

s1 = {1, 2, 3, 4}
s2 = {4, 5, 6}
s3 = {4, 7, 8, 9}

print("interseção", s1 & s2)
print("união", s1 | s2)
print("diferença", s1 - s3)
print("diferença", s3 - s1)
print("diferença simétrica", s1 ^ s3)
