max = 0
with open("data/1.txt", 'r', encoding = 'utf-8') as f:
    arr = []
    for line in f:
        if line.strip() == "":
            total = sum(arr)
            max = total if max < total else max
            arr.clear()
        else:
            arr.append(int(line))

print(max)