with open("data/4.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().splitlines()

    o = 0

    for i in input:
        l,r = i.split(',')
        ls, lr = [int(i) for i in l.split('-')]
        rs, rr = [int(i) for i in r.split('-')]

        if (ls <= rs and lr >= rr) or (rs <= ls and rr >= lr ):
            o+=1
        
    print (o)