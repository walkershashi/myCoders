
def isFloat(string):
    if '.' not in string or string.count('.') >= 2:
        return False
    try:
        float_num = float(string)

    except:
        return False

    return True

t= int(input())
for _ in range(t):
    string = input()
    print(isFloat(string))

