with open("data/6.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().splitlines()
    input = input[0]

    for p in range(4, len(input)):
        packet = input[p-4:p]
        if len(set(packet)) == 4:
            print(packet)
            print(p)
            break

    