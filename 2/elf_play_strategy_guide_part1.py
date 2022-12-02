
rules = {}
rules['A'] = {}
rules['B'] = {}
rules['C'] = {}

rules['A']['X'] = 'D'
rules['A']['Y'] = 'W'
rules['A']['Z'] = 'L'

rules['B']['X'] = 'L'
rules['B']['Y'] = 'D'
rules['B']['Z'] = 'W'

rules['C']['X'] = 'W'
rules['C']['Y'] = 'L'
rules['C']['Z'] = 'D'

score = {}

score['X'] = 1
score['Y'] = 2
score['Z'] = 3
score['W'] = 6
score['L'] = 0
score['D'] = 3

def play (p1, p2):
    return rules[p1][p2]

def scores(p1, p2, r):
    return score[p2] + score[r]

with open("2/data.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().splitlines()
    # print(input)

    result = [] 
    
    for i in input:
        # print(i)
        player1, player2 = i.split(' ')
        outcome = play(player1, player2)
        total_score = scores(player1, player2,outcome)
        result.append([player1, player2, outcome, total_score])
    
    print(result)
    
    player_scores = [i[-1] for i in result]
    print(player_scores)
    print(sum(player_scores))