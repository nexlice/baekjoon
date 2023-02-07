modList = []
for i in range(10):
    modList.append(((int)(input())) % 42)
print(len(set(modList)))