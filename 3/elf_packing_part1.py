def nmap(c):
    if c.islower():
        return ord(c) - 96
    if c.isupper():
        return ord(c) - 64 + 26
    return 0

with open("data/3.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().splitlines()
    
    out = [(v[:len(v)//2], v[len(v)//2:]) for v in input]
    out = [set(l).intersection(r).pop() for l, r in out]
    out = [nmap(i) for i in out]

    print(sum(out))