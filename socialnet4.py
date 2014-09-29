def path_to_friend(network, user_A, user_B):
    # your RECURSIVE solution here!
    return p2f(network, user_A, user_B, [])
 
def p2f(network, user_A, user_B, passed):
    # your RECURSIVE solution here!
    nexts = network[user_A]
    if user_B in nexts:
        return [user_A,user_B]
    for n in nexts:
        if n not in passed:
            passed.append(n)
            path = p2f(network,n, user_B, passed)
            if path:
                return [user_A] + path
    return
 
network = {4:[3,1], 3:[4,4], 2:[], 1: [2]}
print path_to_friend(network, 4, 2)