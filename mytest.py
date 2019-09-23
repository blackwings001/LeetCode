import os
a = ["a", "b", "c"]

result = {}

for i in range(3):
    result[i] = result.get(i, []) + [a[i]]

print(result)

print(os.getcwd())

b = list(range(10))
for i in range(5):
    print(b)
    b.pop(i)
    print(b)

for i in range(6, -1, -1):
    print(i)

s = " "
if s != " ":
    print("s存在")