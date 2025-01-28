l1 = [2, 4, 3]
l2 = [5, 6, 4]
# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]

a = "".join([str(x) for x in l1[::-1]])
b = "".join([str(x) for x in l2[::-1]])
s = str(int(a) + int(b))[::-1]

print(f's: {s}')
