# Enter your code here. Read input from STDIN. Print output to STDOUT

UPPER = set('QWERTYUIOPASDFGHJKLZXCVBNM')
LOWER = set('qwertyuiopasdfghjklzxcvbnm')
DIGIT = set('1234567890')
ALPHA = set('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')

def isValid(emp_uid):
    
    if len(emp_uid) == 10:
        if any(emp_uid.count(i) >= 2 for i in emp_uid):
            return False
            
        else:
            if len(set(emp_uid).intersection(UPPER)) >= 2:
                if len(set(emp_uid).intersection(DIGIT)) >= 3:
                    if all(i in ALPHA for i in emp_uid):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    else:
        return False
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        UID = input()
        res = isValid(UID)
        if res:
            print("Valid")
        else:
            print("Invalid")

