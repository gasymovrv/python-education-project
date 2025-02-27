# Create generator and destruct it
generator = (int(i) for i in input().split(sep=","))
a, b, c, d = generator

print("\t", end="")
for i in range(c, d + 1):
    print(i, end="\t")
print()

for i in range(a, b + 1):
    print(i, end="\t")
    for j in range(c, d + 1):
        print(i * j, end="\t")
    print()
