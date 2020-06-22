import math

def encrypt(s):
    res = []
    size = len(s)

    str_size = str(math.sqrt(size))
    
    if len(str_size) == 3:
        row = int(math.sqrt(size))
        col = int(math.sqrt(size))

    else:
        row = int(math.sqrt(size))
        col = int(math.sqrt(size) + 1)

    if row*col < size:
        row += 1
    
    i = 0
    for it in range(size//col):
        res.append(s[i: col+i])
        i += col
       
    if size//col != row:
        left_str = size - col * (size//col)
        string = s[-left_str:]
        space_len = col - len(string)
        
        for i in range(space_len):
            string += ' '

        res.append(string)
    
    encrypted_string = []
    for i in range(len(res[0])):
        s = ''
        for word in res:
            s += word[i]
        encrypted_string.append(s.replace(" ", ""))
    return encrypted_string


if __name__ == "__main__" : 
    s = input()
    res = encrypt(s)

    print(" ".join(res))    
