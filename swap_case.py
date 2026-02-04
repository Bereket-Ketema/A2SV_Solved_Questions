def swap_case(s):
    r = list(s)
    for i in range(len(r)):
        if r[i].isalpha():
            if r[i].islower():
                r[i] = r[i].upper()
            else:
                r[i] = r[i].lower()
        else:
            r[i] = r[i]
    return ''.join(r)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
