max = []
with open("data/1.txt", 'r', encoding = 'utf-8') as f:
    arr = []
    for line in f:
        if line.strip() == "":
            total = sum(arr)
            max.append(total)
            arr.clear()
        else:
            arr.append(int(line))
max.sort()
max.reverse()

print(sum(max[:3]))
