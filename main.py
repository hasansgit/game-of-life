M, N = 20, 60
dead = "."
alive = "@"
neigbors = (
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
)

R2 = []


def draw():
    print("\033[H\033[J", end="")
    for row in R2:
        print("".join(row))


def isAlive(x, y):
    if x < 0 and y < 0:
        return R2[M - 1][N - 1] == alive
    if x < 0:
        return R2[M - 1][y % N] == alive
    if y < 0:
        return R2[x % M][N - 1] == alive
    return R2[x % M][y % N] == alive


def emulate():
    from copy import deepcopy

    next_gen = deepcopy(R2)
    for i in range(M):
        for j in range(N):
            alive_neighbors = 0
            for x, y in neigbors:
                alive_neighbors += isAlive(i + x, j + y)
            if isAlive(i, j):
                next_gen[i][j] = alive if alive_neighbors in (2, 3) else dead
            else:
                next_gen[i][j] = alive if alive_neighbors == 3 else dead
    return next_gen


def get_hash(gen):
    return hash(tuple(tuple(a for a in row) for row in gen))


def main():
    from time import sleep
    from random import randint

    global R2
    R2 = [[dead if randint(0, 5) else alive for _ in range(N)] for _ in range(M)]

    configs = set()
    configs.add(get_hash(tuple(tuple(dead for _ in range(N)) for _ in range(M))))

    while True:
        draw()
        next_gen = emulate()
        R2 = next_gen
        if get_hash(next_gen) in configs:
            draw()
            break
        configs.add(get_hash(next_gen))
        sleep(0.07)


if __name__ == "__main__":
    main()
