dict1 = {
    "name":"praseesh",
    "age" : 21,
    "place": "kannur"
}
dict1["name"] = "aron"

print (dict1)
list1 = [1,2,4,5]

list1.insert(2,"new") 
list1.remove(10)

set1 = {1,2,3,4}
set2 = {4,6,7,8}

print(set1.union(set2))

for i, j in dict1.items():
    print(i, j)
 
a = lambda x: x+5

print(a(5))
    

class Abc:

    def __init__(self):
        self.a = a
        self.b = b
    
    def sum (self):
        sum  = self.a+self.b
        print(f"sum : {sum}")
a = 5
b = 10 
obj = Abc()
obj.sum()
