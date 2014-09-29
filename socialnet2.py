def path_to_friend(network, user_A, user_B, passed=None):
    # your RECURSIVE solution here!
    if user_A not in network or user_B not in network:
        return None
    nexts = network[user_A]
    if passed is None:
        passed = []
    if user_A == user_B:
        return [user_A]
    if user_B in nexts:
        return [user_A, user_B]
    passed.append(user_A)
    for n in nexts:
        if n not in passed:
            path = path_to_friend(network, n, user_B,passed)
            if path:
                return [user_A] + path
    return

network = {'0' : ['3', '6', '8'],
               '1' : ['5', '6', '7'],
               '2' : ['0', '1', '3', '4', '6', '7', '8', '9'],
               '3' : ['4'],
               '4' : ['0', '1', '3', '6', '8'],
               '5' : ['1', '6', '8', '9'],
               '6' : ['0', '2', '7', '9'],
               '7' : ['4', '9'],
               '8' : ['0', '1', '2', '3'],
               '9' : ['2', '3', '6', '7', '8']}
print path_to_friend(network, '4', '2')