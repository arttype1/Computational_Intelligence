# Exercises and examples from 'Computational Intelligence' by Poole, Mackworth, and Goebel
# all code by George A. Merrill, except where otherwise noted.
##########################################################################################
# exercise 2.4 ground atomic conequences derivable from a knowledge base


# terms #######################################
terms = ['a', 'b', 'c', 'd', 'e']
# facts #######################################
r = ['e']
p = ['c']
s = [('a', 'b'), ('d', 'b'), ('e', 'd')]
q = ['b']
# Rules #######################################
# p(X) if q(X) and r(X)
# q(X) if s(X,Y) and  q(Y)

# Use a Bottom-Up Ground Proof Procedure
def bottom_up():
    mode = 'run'
    while mode == 'run':
        mode = 'done'
        #  rules are checked
        # rule1
        for x in terms:
            if x not in p and x in q and x in r:
                p.append(x)
                mode = 'run'
        # rule2
        for x in terms:
            if x not in q:
                for y in terms:
                    if (x, y) in s and y in q:
                        q.append(x)
                        mode = 'run'


bottom_up()
for rx in r:
    print(f' r({rx}) holds')
for qx in q:
    print(f' q({qx}) holds')
for px in p:
    print(f' p({px}) holds')
for sx in s:
    print(f' s({sx}) holds')


