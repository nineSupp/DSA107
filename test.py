x : dict[str, int] = {"Nine": 2, "Pheem": 3, "Paing": 4}
print(x)

for i in x:
    print(i)


for i in x.values():
    print(i)


for i, j in x.items():
    print(i, j)

print(x["Pheem"])

x["Pheem"] += 1

print(x["Pheem"])