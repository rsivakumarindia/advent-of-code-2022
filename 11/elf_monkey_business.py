from __future__ import annotations
import re

reduce_by_3 = True

class Item:

    def __init__(self, value) -> None:
        self.value = value
        self.original = value
    
    def inspect(self, operator, value):
        if 'old' == value:
            v = self.value
        else:
            v = int(value)

        if '+' == operator:
            self.value += v
        elif '*' == operator:
            self.value *= v

        # print(f"Worry level is multiplied by {v} to {self.value}.")

    def relief(self, monkeys):
        global reduce_by_3 
        if reduce_by_3:
            self.value = self.value // 3
            # print(f"Monkey gets bored with item. Worry level is divided by 3 to {self.value}.")
        else:
            mod = 1
            for m in monkeys:
                mod *= monkeys[m].divisor
            self.value = self.value % mod

class Monkey:
    
    items : list(Item)
    inspect_cnt : int

    def __init__(self, number: int) -> None:
        self.number = number
        self.inspect_cnt = 0
    
    def starting_items(self, items):
        self.items = [Item(int(i)) for i in items]

    def add_item(self, item):
        self.items.append(item)
    
    def operation(self, operator, operand):
        self.operator = operator
        self.operand = operand
    
    def divisibleby(self, divisor: int):
        self.divisor = int(divisor)

    def ifTrue(self, trueMonkey):
        self.trueMonkey = trueMonkey
    
    def ifFalse(self, falseMonkey):
        self.falseMonkey = falseMonkey
    
    def inspects(self, item:Item, monkeys):
        # print(f"Monkey inspects an item with a worry level of {item.value}.")
        item.inspect(self.operator, self.operand)
        item.relief(monkeys)
        self.inspect_cnt += 1

    def test(self, item: Item, monkeys):
        transfer_to = None
        if item.value % self.divisor == 0:
            # print(f"Current worry level is divisible by {self.divisor}.")
            transfer_to = self.trueMonkey
        else:
            # print(f"Current worry level is not divisible by {self.divisor}.")
            transfer_to = self.falseMonkey
        
        monkeys[transfer_to].add_item(item)
        # print(f"Item with worry level {item.value} is thrown to monkey {transfer_to}.")
    
    def do_round(self, monkeys):
        for _ in range(len(self.items)): 
            item = self.items.pop(0)
            self.inspects(item, monkeys)
            self.test(item, monkeys)


def notes(lines):
    monkeys = []
    
    for note in '\n'.join(lines).split('\n\n'):
        monkey_number = re.search(r"Monkey (\d+)", note).group(1)
        starting_items = re.search(r"Starting items: (\d+(?:, \d+)*)", note).group(1).split(', ')
        operation = re.search(r"Operation: (\w+) = old (.*) (\w+)", note).group(2)
        operand = re.search(r"Operation: (\w+) = old (.*) (\w+)", note).group(3)
        divisor = re.search(r"divisible by (\d+)", note).group(1)
        true_monkey = re.search(r"If true: throw to monkey (\d+)", note).group(1)
        false_monkey = re.search(r"If false: throw to monkey (\d+)", note).group(1)

        m = Monkey(int(monkey_number))
        m.starting_items(starting_items)
        m.operation(operation, operand)
        m.divisibleby(divisor)
        m.ifTrue(int(true_monkey))
        m.ifFalse(int(false_monkey))
        
        monkeys.append(m)

    return {m.number : m for m in monkeys}

def round(monkeys):
    for i in monkeys.keys():
        # print(f"Monkey {i}:")
        monkeys[i].do_round(monkeys)
        # print()
    
    # for m in monkeys.keys():
        # print(f"Monkey {m}: {', '.join([str(i.value) for i in monkeys[m].items])}")


def monkey_business_round(lines, rounds):
    monkeys = notes(lines)

    for i in range(rounds):
        round(monkeys)

    # print()

    # for m in monkeys.keys():
        # print(f"Monkey {m} inspected items {monkeys[m].inspect_cnt} times.")

    monkey_business = sorted([monkeys[m].inspect_cnt for m in monkeys.keys()])
    
    print(monkey_business[-1] * monkey_business[-2])

def p1(lines):
    global reduce_by_3 
    reduce_by_3 = True
    monkey_business_round(lines, 20)
    # print('==========')

def p2(lines):
    global reduce_by_3 
    reduce_by_3 = False
    monkey_business_round(lines, 10000)
    # print('==========')

with open("data/11.txt", 'r', encoding = 'utf-8') as f:
    lines = f.read().splitlines()

    p1(lines)
    p2(lines)