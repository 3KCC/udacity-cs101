def path_to_friend(network, user, connection):
    # your RECURSIVE solution here!
    return p2f2(network, user, connection, [])
 
def p2f2(network, user, connection, history):
    # your RECURSIVE solution here!
    cont = network[user]
    for x in cont:
        if x == connection:
            return [x]
        elif not x in history:
            history.append(x)
            v = p2f2(network,x, connection, history)
            if v != None:
                return [x] + v
    return
 
network = {4:[3,1], 3:[4,4], 2:[], 1: [2]}
print path_to_friend(network, 4, 2)