with open("test.txt", "w") as f:
    f.write("Expence 1\n")
    f.write("Expence 2\n")
    f.write("Expence 3\n")


with open("test.txt", "r") as f:
    content = f.readlines()


for i in content:
    print(i.strip())