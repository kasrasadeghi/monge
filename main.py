def monge(m) -> bool:
    results = []
    for i in range(len(m) - 1):
        tops = []
        bots = []
        comps = []
        for j in range(len(m[0]) - 1):
            A = m[i][j]    ; B = m[i][j + 1]
            C = m[i + 1][j]; D = m[i + 1][j + 1]
            top = "%2d %2d   " % (A, B)
            bot = "%2d %2d   " % (C, D)
            result = A + D <= B + C
            comp = "%2d%s%2d   " % (A + D, "≤" if A + D <= B + C else ">", B + C)
            tops.append(top)
            bots.append(bot)
            comps.append(comp)
            results.append(result)
        print("".join(tops))
        print("".join(bots))
        print("".join(comps))
    return all(results)


def main():
    m = ["37 23 22 32",
         "21 6 5 10",
         "53 34 30 31",
         "32 13 9 6",
         "43 21 15 8"]

    m = [[int(x) for x in el.split(' ')] for el in m]

    print(monge(m))


if __name__ == '__main__':
    main()
