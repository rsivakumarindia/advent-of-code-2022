stack = ['JZGVTDBN','FPWDMRS','ZSRCV','GHPZJTR','FQZDNJCT','MFSGWPVN','QPBVCG','NPBZ','JPW']
stack = [list(reversed([*i])) for i in stack]
print(stack)


with open("data/5.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().split('\n\n')[1].splitlines()

    for line in input:
        arr = line.split(' ')
        count, fst, tst = [int(arr[i]) for i in range(0, len(arr)) if i in [1,3,5]]
                
        x = stack[fst-1][-count:]
        del stack[fst-1][-count:]
        stack[tst-1].extend(x)

    print(stack)

    out = [i[-1] for i in stack]

    print(''.join(out))