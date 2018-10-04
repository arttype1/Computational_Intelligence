# Exercises and examples from 'Computational Intelligence' by Poole, Mackworth, and Goebel
# all code by George A. Merrill, except where otherwise noted.
# version_001 can answer queries about basic facts
##########################################################################################
# case_study 3_2 House Wiring
import re
logic_vars = re.compile('[_A-Z]+') # used to tell if a word is a variable
# facts #######################################
light = [['l1'], ['l2']]
up = [['s2'], ['s3']]
down = [['s1']]
ok = [['l1'], ['l2'], ['cb1'], ['cb2']]
c1 = ['l1', 'w0']
c2 = ['l2', 'w4']
c3 = ['w5', 'outside']
# Rules #######################################
r1 = [['w0', 'w1'], ['up', 's2']]
r2 = [['w0', 'w2'], ['down', 's2']]
r3 = [['w1', 'w3'], ['up', 's1']]
r4 = [['w2', 'w3'], ['down', 's1']]
r5 = [['w4', 'w3'], ['up', 's3']]
r6 = [['w0', 'w1'], ['ok',  'cb1']]
r7 = [['w6', 'w5'], ['ok', 'cb2']]
# lookups ######################################
connected_to = [c1, c2, c3]
r_conn = [r1, r2, r3, r4, r5, r6, r7]
rules = {'connected_to': r_conn}
facts = {'light': light, 'up': up, 'down': down, 'ok': ok, 'connected_to': connected_to}


def match(clause1, clause2):
    # if str(clause1) == str(clause2):
    #     print(f'{clause1}, {clause2}')
    #     print('found match')
    #     return True
    if len(clause1) != len(clause2):
        print('not same size')
        return False
    else:
        for i in range(len(clause1)):
            if not logic_vars.match(clause2[i]) and not logic_vars.match(clause1[i]):
                if str(clause1[i]) != str(clause2[i]) and not logic_vars.match(clause1[i]):
                    return False
        else:
            return True


def outcome(head):
    if len(head) != 1:
        return [item for item in facts[head[0]] if match(item,head[1])]
    else:
        return []


query = input('query: ')
quest = re.sub('\)', '',query).split('(')
tempq = quest.pop().split(', ')
quest.append(tempq)
ans = outcome(quest)
if len(ans) != 0:
    for item in ans:
        print(f'True {item} is {quest[0]}')
else:
    print('False')
