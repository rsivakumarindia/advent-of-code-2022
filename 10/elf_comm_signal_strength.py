def p1(lines):

    ss = [20, 60, 100, 140, 180, 220]
    cycle = 0
    X = 1
    result = []
    for i in range(len(lines)):
        cmds = lines[i].strip().split()
        if len(cmds) == 1:
            cycle +=1
            if cycle in ss:
                result.append([cycle, X])
        else:
            cmd, val = cmds
            for i in range(2):
                cycle+=1
                if cycle in ss:
                    result.append([cycle, X])
            X+=int(val)

    print(sum([a[0] * a[1] for a in result]))

def p2(lines):

    X = 1
    sprite = [X-1, X, X+1]
    l = 40
    h = 6
    crt = [['' for j in range(l)] for i in range(h)]

    cycle = 0
    cmd_cycle = 0
    lit = '#'
    dark = '.'
    
    lineIter = iter(lines)
    complete_cycle = {'noop': 1, 'addx': 2}
    
    line = next(lineIter, None)    
    while line:
        cycle +=1
        cmd_cycle+=1

        cmds = line.strip().split()
        cmd = cmds[0]

        x, y = (cycle-1) // l, ( cycle-1) % l
        if y in sprite:
            crt[x][y] = lit
        else:
            crt[x][y] = dark

        if complete_cycle[cmd] == cmd_cycle:
            cmd_cycle = 0
            if cmd == 'addx':
                X+=int(cmds[1])
                sprite = [X-1, X, X+1]
            
            line = next(lineIter, None)
    show(crt)

def show(crt):
    for row in crt:
        print(' '.join(map(str, row)))

    print()

with open("data/10.txt", 'r', encoding = 'utf-8') as f:
    lines = f.read().splitlines()

    p1(lines)
    p2(lines)