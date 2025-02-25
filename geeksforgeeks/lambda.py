numbers = [1, 2, 3, 4, 5]
s = [(lambda x: x**2)(x) for x in numbers]
for i in s:
    print(i)
d = [(lambda x: x)(x) for x in numbers if x % 2 == 0]
print(d)
names = ["John", "Alice", "Bob", "Charlie", "David"]
names = sorted(names, key=lambda x: len(x))
print(names)
