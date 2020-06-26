def checkPassword(string):
    size = 0
    if len(string) < 6:
        size = 6 - len(string)

    cnt = 0
    string = set(string)
    number = set(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    sp_char = set("!@#$%^&*()-+")

    if len(string.intersection(number)) == 0:
        cnt += 1

    if len(string.intersection(lower_case)) == 0:
        cnt += 1

    if len(string.intersection(upper_case)) == 0:
        cnt += 1

    if len(string.intersection(sp_char)) == 0:
        cnt += 1

    return max(cnt, size)

if __name__ == "__main__":
    n = int(input())
    password = input()

    res = checkPassword(password)
    print(res)

