
rules = {}
rules['R'] = {}
rules['P'] = {}
rules['S'] = {}

rules['R']['R'] = 'D'
rules['R']['P'] = 'W'
rules['R']['S'] = 'L'

rules['P']['R'] = 'L'
rules['P']['P'] = 'D'
rules['P']['S'] = 'W'

rules['S']['R'] = 'W'
rules['S']['P'] = 'L'
rules['S']['S'] = 'D'

outcome_to_position = lambda d: dict(zip(d.values(), d.keys()))

new_rules = {}
for rk, rv in rules.items():
    rules[rk] = outcome_to_position(rv)

print(rules)

def position(p1, out):
    return rules[mapping[p1]][mapping[out]]

mapping = {}
mapping['A'] = 'R'
mapping['B'] = 'P'
mapping['C'] = 'S'
mapping['X'] = 'L'
mapping['Y'] = 'D'
mapping['Z'] = 'W'

reverse_mapping = outcome_to_position(mapping)

score = {}

score['X'] = 0
score['Y'] = 3
score['Z'] = 6
score['R'] = 1
score['P'] = 2
score['S'] = 3

def scores(p1, r, p2):
    return score[p2] + score[r]

print(reverse_mapping)
with open("2/data.txt", 'r', encoding = 'utf-8') as f:
    input = f.read().splitlines()
    # print(input)

    result = [] 
    
    for i in input:
        # print(i)

        player1, outcome = i.split(' ')
        player2 = position(player1, outcome)
        result.append([player1, outcome, player2, scores(player1,player2, outcome)])
        
    player_scores = [i[-1] for i in result]
    print(player_scores)
    print(sum(player_scores))