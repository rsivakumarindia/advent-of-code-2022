with open("data/6.txt", 'r', encoding = 'utf-8') as f:
    input = f.read()
    
    for p in range(14, len(input)):
        packet = input[p-14:p]
        if len(set(packet)) == 14:
            print(packet)
            print(p)
            break

    