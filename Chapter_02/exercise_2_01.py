# Exercises and examples from 'Computational Intelligence' by Poole, Mackworth, and Goebel
##########################################################################################
# exercise 2.1 model of a knowledge base
facts = ['e', ' ']
rules = [('a', 'b', 'c'), ('a', 'e', 'f'), ('b', 'd', ' '), ('c', 'e', ' '), ('d', 'h', ' '),
         ('f', 'g', ' '), ('g', 'c', ' ')]


def outcome(head):
    if head in facts:
        return True
    else:
        body = [item for item in rules if item[0] == head]
        for i in body:
            if outcome(i[1]) and outcome(i[2]):
                return True
        else:
            return False


alpha = ['a','b','c','d','e','f','g','h']
for atom in alpha:
    print(f'{atom} : {outcome(atom)}')
