from itertools import permutations


def solve_cryptarithmetic():
    S, E, N, D = 9, 5, 6, 7
    M, O, R, Y = 1, 0, 8, 2

    send = 1000 * S + 100 * E + 10 * N + D
    more = 1000 * M + 100 * O + 10 * R + E
    money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

    if send + more == money:
        return (send, more, money)

    return None

solution = solve_cryptarithmetic()
if solution:
    send, more, money = solution
    print("Send =", send)
    print("More =", more)
    print("Money =", money)
else:
    print("Não foi encontrada uma solução válida.")
