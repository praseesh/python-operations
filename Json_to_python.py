
import json

# some JSON:
x =  '{ "name":" John", "age":30, "city":"New York"}'

y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])
print(y)
