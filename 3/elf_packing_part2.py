def nmap(c):
    if c.islower():
        return ord(c) - 96
    if c.isupper():
        return ord(c) - 64 + 26
    return 0

with open("data/3.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().splitlines()

    out = [input[i: i+3] for i in range(0, len(input), 3)]
    out = [set(l[0]) & set(l[1]) & set(l[2])  for l in out ]
    out = [nmap(s.pop()) for s in out]

    print(sum(out))