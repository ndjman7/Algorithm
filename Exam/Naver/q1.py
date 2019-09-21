
drum = ['######', '>#*###', '####*#', '#<#>>#', '>#*#*<', '######']


def solution(drum):
    answer = 0

    Y = len(drum)
    X = len(drum[0])

    def f(y, x, star):
        if y == Y - 1:
            return True

        d = drum[y][x]
        if d == '#':
            return f(y+1 , x, star)

        if d == '>':
            if x+1 >= X:
                return False
            return f(y, x+1, star)

        if d == '<':
            if x-1 < 0:
                return False
            return f(y, x-1, star)

        if d == '*':
            if star:
                return f(y+1, x, False)
            else:
                return False


    for s in range(X):
        a = f(0, s, True)
        if a:
            answer += 1

    return answer

print(solution(drum))
