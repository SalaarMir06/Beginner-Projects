if __name__ == '__main__':
    N = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        N.append([name, score])

    scores = sorted(set([student[1] for student in N]))
    second_lowest = scores[1]

    names = sorted([student[0] for student in N if student[1] == second_lowest])

    for name in names:
        print(name)

