from functools import reduce

max_height = lambda l : max(l) if len(l) > 0 else -1

def p1(grid):
    
    visible_trees = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            tree = grid[row][col]

            right = [grid[row][i] for i in range(col+1, len(grid[row]))]
            left = list(reversed([grid[row][i] for i in range(col)]))
            top = list(reversed([grid[i][col] for i in range(row)]))
            down = [grid[i][col] for i in range(row+1, len(grid))]
            
            s = [max_height(i) for i in [left, right, top, down]]
            if tree > min(s):
                visible_trees+=1

    print(visible_trees)

def scenic_score(t, l):
    if not l:
        return 0;
    else:
        d = 0
        for i in l:
            d +=1
            if i >= t:
                break;
        return d

def p2(grid):
    max_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            tree = grid[row][col]

            right = [grid[row][i] for i in range(col+1, len(grid[row]))]
            left = list(reversed([grid[row][i] for i in range(col)]))
            top = list(reversed([grid[i][col] for i in range(row)]))
            down = [grid[i][col] for i in range(row+1, len(grid))]

            score = [scenic_score(tree, i) for i in [left, right, top, down]]

            result = reduce(lambda x, y: x * y, score)

            max_score = max([max_score, result])
    
    print(max_score)


with open("data/8.txt", 'r', encoding = 'utf-8') as f:
    lines = f.read().splitlines()

    grid = [[ int(j) for j in list(i)] for i in lines]

    p1(grid)
    p2(grid)