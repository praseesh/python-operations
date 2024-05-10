tup = ("Apple", "Mango", 2,3,4,3 )
print(tup)
a = tup[1:4]
print(a)

b = list(tup)
print(b)
b[1] = "Banana"
b.append("Orange")
b.insert(2, "Cherry")
print(b)
b.remove("Apple")
print(b)
tup = tuple(b)
print(tup)