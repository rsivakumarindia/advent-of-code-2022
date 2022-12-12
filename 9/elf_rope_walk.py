def adjust(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

def movetail(head, tail):
    x = head[0] - tail[0]
    y = head[1] - tail[1]

    if abs(x) < 2 and abs(y) < 2:
        return
    else:
        tail[0] += adjust(head[0], tail[0])
        tail[1] += adjust(head[1], tail[1])

    return tail

def p1(lines):
    start = [0,0]

    rope = [list(start) for i in range(2)]
    head, tail = rope

    tail_pos = [list(tail)]

    for line in lines:
        dir, step = line.split()
        step = int(step)
        
        for i in range(0, step):
            if dir == 'R':
                head[0] += 1
            elif dir == 'L':
                head[0] -= 1
            elif dir == 'U':
                head[1] += 1
            elif dir == 'D':
                head[1] -= 1
            movetail(head, tail)
            tail_pos.append(list(tail))

    print(len(set([tuple(i) for i in tail_pos])))

def p2(lines):
    start = [0,0]

    rope = [list(start) for i in range(10)]
    
    head = rope[0]
    tail = rope[-1]

    tail_pos = [list(tail)]

    for line in lines:
        dir, step = line.split()
        step = int(step)
        
        for i in range(0, step):
            if dir == 'R':
                head[0] += 1
            elif dir == 'L':
                head[0] -= 1
            elif dir == 'U':
                head[1] += 1
            elif dir == 'D':
                head[1] -= 1
            for j in range(1, len(rope)):
                movetail(rope[j-1], rope[j])
            # print(rope)
            tail_pos.append(list(tail))

    print(len(set([tuple(i) for i in tail_pos])))

with open("data/9.txt", 'r', encoding = 'utf-8') as f:
    lines = f.read().splitlines()

    p1(lines)
    p2(lines)